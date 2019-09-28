import sys
import os
import getopt
import hmac
import hashlib

def verificadorPasta(pasta): # Função que verifica se a string passada é um diretório ou não
    if os.path.isdir(pasta):
        return 0
    return -1

def i(pasta,saida, metodo):
    if saida != "Default":
        arq_save = open(saida, "w")
    files = []
    for r, d, f in os.walk(pasta):
        for file in f:
            files.append(os.path.join(r, file)) 
    for f in files:
        arq_aberto = open(f,"rb")
        print(f)
        sha256 = hashlib.sha256()
        while True:
            data = arq_aberto.read(655)
            if not data:
                break
            sha256.update(data)
        arq_aberto.close()
        arq_save.write(f+" > "+sha256.hexdigest()+"\n")
    arq_save.close()

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
