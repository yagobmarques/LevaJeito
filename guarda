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
        data = arquivo.read(65534) # Lê em chunks, para não estourar o buffer
        if not data:
            break
        sha256.update(data)
    return sha256.hexdigest()


def hmacArquivo(arquivo,senha): # Gera a Hash de um arquivo a partir de uma senha
    sha256 = hmac.new(senha.encode("utf-8"))
    while True:
        data = arquivo.read(65534) # Lê em chunks, para não estourar o buffer
        if not data:
            break
        sha256.update(data)
    return sha256.hexdigest()


def allFiles(pasta): # Joga todos os nomes dos arquivos (recursivamente) a partir de um um nó raiz em um vetor
    files = []
    for r, d, f in os.walk(pasta): 
        for file in f:
            files.append(os.path.join(r, file)) 
    return files


def i(pasta,saida, metodo): # Função que gera o arquivo <path>.guarda com "<nome_arq> > <hash>"
    if saida != "Default":
        arq_saida = open(saida, "w")
    files = allFiles(pasta) # Vetor com todos os arquivos de uma pasta e suas subpastas
    arq_oculto = open(pasta+".guarda", "w") # Arquivo com os dados a serem comparados à posteriori
    for f in files: # Percorre todos os arquvos recursivamente
        arq_aberto = open(f,"rb")
        if metodo == "hash": # Encriptando como hash comum
            hash_arq = hashArquivo(arq_aberto)
        if metodo[:4] == "hmac": # Encriptando com Hmac
            hash_arq = hmacArquivo(arq_aberto, metodo[4:])
        arq_aberto.close()
        if saida != "Default":
            arq_saida.write(f+" > "+hash_arq+"\n") # Joga no arquivo de saida o resultado <file> > <hash>
        else:
            print(f+" > "+hash_arq+"\n") # Saida padrão
        arq_oculto.write(f+" > "+hash_arq+"\n") # Arquivo oculto <path>.guarda
    if saida != "Default":
        arq_saida.close() # Fechando arquivo de saída do usuário    
    arq_oculto.close() # Fechando <path>.guarda


def mountDictByGuarda(pasta,saida): # Monta um dicionário <arquivo>:<hash> a partir do arquivo ".guarda"
    dicio = {}
    if saida != "Default":
        arq_sada = open(saida, "w") 
    try: # Tenta pegar a o arquivo <path>.guarda
        dados = open(pasta+".guarda","r")
    except: # Caso o .guarda ainda não exista. OU seja, a pasta em questão não foi monitorada
        if saida!="Default":
            arq_saida.write("A pasta não está sendo monitorada!")
            arq_saida.close()
        else:
            print("A pasta em questão não está sendo monitorada")
        return None
    lines = dados.readlines()
    for line in lines: # Montando o dicionário
        data = line.split(" > ") # Separador padrão que defini no escorpo "<file> > <hash>"
        dicio[data[0]] = data[1][:len(data[1])-2] # <file_name>:<hash> obs: -2 para não pegar o '\n'
    return dicio


def mountDictByPath(pasta, metodo): # Monta um dicionário  <arquivo>:<hash> a partir de uma pasta raiz 
    # Diferente do ByPasta, nesse precisamos gerar a hash para comparar à posterióri
    files = allFiles(pasta)
    dicio = {}
    for f in files:
        arq_aberto = open (f, "rb")
        if metodo == "hash": # Gerando a Hash do Arquivo
            hash_arq = hashArquivo(arq_aberto)
        if metodo[:4] == "hmac": # Gerando a Hash Hmac do Arquivo
            hash_arq = hmacArquivo(arq_aberto,metodo[4:]) 
        arq_aberto.close()
        dicio[f]=hash_arq[:len(hash_arq)-1] # Montando o dicionário
    return dicio


def t(pasta, saida, metodo): # Tracking dos arquivos
    # Para saídas em arquivo: [N] = Novo, [A] = Alterado e [R] = Removido
    # Para a saída padrão: Verde = Novo, Amarelo = Alterado e Vermelho = Removido
    dicioAntigo = mountDictByGuarda(pasta,saida) # Monta o dicinário pelo arquivo <path>.guarda
    if dicioAntigo == None:
        # Verificação para não fazer o tracking em uma pasta que não é monitorada
        return -1
    dicioAtual = mountDictByPath(pasta,metodo) # Monta o dicionário refazendo as hash's no exato momento
    dicioSave = dicioAtual
    alterados = [] # Vetor para guardar os nomes dos arquivos alterados
    novos = [] # Vetor para guardar os nomes dos arquivos novos
    excluidos = [] # Vetor para guardar os nomes dos arquivos excluidos
    normais = [] # Vetor para guardar os nomes dos arquivos normais
    for j in dicioAntigo:
        if j not in dicioAtual:
            # Se ele não está na nova varredura, então ele foi excluído
            excluidos.append(j)
        if j in dicioAtual and dicioAntigo[j] != dicioAtual[j]and j !=pasta+".guarda":
            # Se ele está mas as hash's não batem, ele foi alterado
            alterados.append(j)
            dicioAtual.pop(j)
        elif j in dicioAtual and dicioAntigo[j] == dicioAtual[j] :
            # Tudo certo
            normais.append(j)
            dicioAtual.pop(j)
    for j in dicioAtual:
        if j != pasta+".guarda":
            # Arquivos que estão na nova varredura mas não estão na antiga
            novos.append(j)
    if saida == "Default":
        printColorido(alterados, novos, excluidos) # Printa na saída padrão
    else: # Joga para o arquivo de saída a saida do tracking
        arq_saida = open(saida, "w")
        for j in novos:
            arq_saida.write("[N]"+j+"\n")
        for j in alterados:
            arq_saida.write("[A]"+j+"\n")
        for j in excluidos:
            arq_saida.write("[R]"+j+"\n")
        arq_saida.close()

def printColorido(alterados,novos,excluidos): # Função para mostrar na tela amigavelmente o resultado do tracking
    red =  "\033[31m" 
    reset = "\033[0m"
    green = "\033[32m"
    yellow = "\033[33m"
    print("\n## Verde => arquivos novos, Amarelo => Arquivos alterados, Vermelho => arquivos excluidos ##\n")
    for j in novos:
        print(green+j+reset)
    for j in alterados:
        print(yellow+j+reset)
    for j in excluidos:
        print(red+j+reset)

def x(pasta,saida): # Função que para o monitoramento da pasta
    try: # Tenta remover <path>.guarda
        os.remove(pasta+".guarda")
        if saida == "Default":
            print(green+"Pasta %s des-monitorada com sucesso!" % (pasta)+reset)
        else:
            arq_saida = open(saida,"w")
            arq_saida.write("Pasta %s des-monitorada com sucesso!" % (pasta))
            arq_saida.close()
    except: # Se não tem o arquivo <path>.guarda, então a pasta não está sendo monitorada
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
try: # Tenta pegar os parâmetros
    optlist,arguments= getopt.gnu_getopt(args,'i:t:x:o:',['hash','hmac=']) 
except: # Se tiver algo a mais, ou faltando
    print("Erro de parâmetros!")
    print(red+"Exit status -1"+reset)
saida = ""
metodo = ""
pasta = ""
opcao = ""
senha = ""
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
if metodo == "" and opcao != "-x": # Caso o suário não digite a criptografia
    print("Parâmetro <metodo> inválido!")
    print(red+"Exit status -1"+reset)
    sys.exit(-1)

print("\n========= Tabela de Configuração ============")
print("Método: " +  metodo)
if metodo == "hmac":
    print("Senha: " + senha)
print("Opção: " + opcao)
print("Pasta: " + pasta)
print("Arquivo de saída: " + saida)
print("=============================================\n")
if opcao == "i": # Executa a varredura
    i(pasta, saida, metodo+senha)
if opcao == "x": # Exclui a pasta
    x(pasta,saida) 
if opcao == "t": # Executa a análise
    t(pasta, saida, metodo+senha)
