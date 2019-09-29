import sys
import os
import getopt
import hmac
import hashlib

def verificadorPasta(pasta): # Função que verifica se a string passada é um diretório ou não
    if os.path.isdir(pasta):
        return 0
    return -1

def hashArquivo(arquivo): # Gera a Hash de um arquivo
    sha256 = hashlib.sha256()
    while True:
        data = arquivo.read(65534)
        if not data:
            break
        sha256.update(data)
    return sha256.hexdigest()

def allFiles(pasta):
    files = []
    for r, d, f in os.walk(pasta):
        for file in f:
            files.append(os.path.join(r, file)) 
    return files

def i(pasta,saida, metodo):
    if saida != "Default":
        arq_saida = open(saida, "w")
    files = allFiles(pasta)
    arq_oculto = open(pasta+".guarda", "w")
    for f in files:
        arq_aberto = open(f,"rb")
        if metodo == "hash":
            hash_arq = hashArquivo(arq_aberto)
        if metodo[:4] == "hmac":
            print("Aqui vai o código de hmac!")
        arq_aberto.close()
        if arq_saida != "Default":
            arq_saida.write(f+" > "+hash_arq+"\n")
        arq_oculto.write(f+" > "+hash_arq+"\n")
    if saida != "Default":
        arq_saida.close()
    arq_oculto.close()

def mountDictByGuarda(pasta,saida):
    dicio = {}
    if saida != "Default":
        arq_sada = open(saida, "w")
    try:
        dados = open(pasta+".guarda","r")
    except:
        if saida!="Default":
            arq_saida.write("A pasta não está sendo monitorada!")
            arq_saida.close()
        else:
            print("A pasta em questão não está sendo monitorada")
        return None
    lines = dados.readlines()
    for line in lines:
        data = line.split(" > ")
        dicio[data[0]] = data[1][:len(data[1])-2]
    return dicio

def mountDictByPath(pasta, metodo):
    files = allFiles(pasta)
    dicio = {}
    for f in files:
        arq_aberto = open (f, "rb")
        if metodo == "hash":
            hash_arq = hashArquivo(arq_aberto)
            arq_aberto.close()
        if metodo[:4] == "hmac":
            print("Aqui vai o código de hmac!")
        dicio[f]=hash_arq[:len(hash_arq)-1]
    return dicio

def t(pasta, saida, metodo):
    dicioAntigo = mountDictByGuarda(pasta,saida)
    dicioAtual = mountDictByPath(pasta,metodo)
    alterados = []
    novos = []
    excluidos = []
    normais = []
    for j in dicioAntigo:
        if j not in dicioAtual:
            excluidos.append(j)
        if j in dicioAtual and dicioAntigo[j] != dicioAtual[j] and j!="./.guarda":
            print("%s & %s" % (dicioAntigo[j], dicioAtual[j]))
            alterados.append(j)
            dicioAtual.pop(j)
        else:
            normais.append(j)
            dicioAtual.pop(j)
            
    for j in dicioAtual:
        novos.append(j)

    print("Alterados: ", alterados)
    print("Novos: ", novos)
    print("Excluidos: ", excluidos)
def x(pasta,saida):
    try:
        os.remove(pasta+".guarda")
        if saida == "Default":
            print(green+"Pasta %s des-monitorada com sucesso!" % (pasta)+reset)
        else:
            arq_saida = open(saida,"w")
            arq_saida.write("Pasta %s des-monitorada com sucesso!" % (pasta))
            arq_saida.close()
    except:
        if saida == "Default":
            print(red+"A pasta %s não está sendo monitorada" % (pasta)+reset)
        else:
            arq_saida = open(saida, "w")
            arq_saida.write("A pasta %s não está sendo monitorada" % (pasta))
            arq_saida.close()
    

# Cores para ficar bonito :)
red =  "\033[31m" 
reset = "\033[0m"
green = "\033[32m"

# Pegando arqumentos passados pelo usuário
args = sys.argv[1:]
try:
    optlist,arguments= getopt.gnu_getopt(args,'i:t:x:o:',['hash','hmac='])
except:
    print("Erro de parâmetros!")
    print(red+"Exit status -1"+reset)
saida = ""
metodo = ""
pasta = ""
opcao = ""

for j in optlist:
    if (j[0]=="--hmac"):
        metodo = "hmac"
        senha = j[1]
    if (j[0]=="--hash"):
        metodo = "hash"
    if (j[0]=="-t"):
        opcao = "t"
        pasta = j[1]
    if (j[0]=="-i"):
        pasta = j[1]
        opcao = "i"
    if (j[0]=="-x"):
        opcao = "x"
        pasta = j[1]
    if (j[0]== "-o"):
        saida = j[1]
    elif saida == "":
        saida = "Default"

# Verificando as entradas dos usuários
if verificadorPasta(pasta):
    print("Parâmetro <pasta> inválido!")
    print(red+"Exit status -1"+reset)
    sys.exit(-1)

print("========= Tabela de Configuração ============")
print("Método: " +  metodo)
if metodo == "hmac":
    print("Senha: " + senha)
print("Opção: " + opcao)
print("Pasta: " + pasta)
print("Arquivo de saída: " + saida)
print("=============================================")
if opcao == "i":
    i(pasta, saida, metodo)
if opcao == "x":
    x(pasta,saida)
if opcao == "t":
    t(pasta, saida, metodo)
