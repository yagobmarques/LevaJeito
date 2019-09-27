import sys
import os
import getopt

def verificadorMetodo(metodo): # Função que retorna -1 se a entrada do método é inválida, 1 se é -hash e 2 se é -hmac
    if metodo == "--hash":
        return 1
    if metodo == "--hmac":
        return 2
    return -1

def verificadorOpcao(opcao): # Função que retorna 1 se -i, 2 se -t, 3 se -x, -1 se qualquer outro
    if opcao == "-i":
        return 1
    if opcao == "-t":
        return 2
    if opcao == "-x":
        return 3
    return -1

def verificadorPasta(pasta): # Função que verifica se a string passada é um diretório ou não
    if os.path.isdir(pasta):
        return 0
    return -1

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
    sys.exit(-1)
optlist,arguments= getopt.gnu_getopt(args,'i:t:x:o:',['hash','hmac='])
print ("Opções: ",optlist)
print ("Argumentos", arguments)
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
    else:
        saida = "tty"

# Verificando as entradas dos usuários
if verificadorPasta(pasta):
    print("Parâmetro <pasta> inválido!")
    print(red+"Exit status -1"+reset)
    sys.exit(-1)
# if verificadorMetodo(metodo) == -1:
#     print("Parâmetro <método> inválido!")
# else:
#     if verificadorMetodo(metodo)==2:
#         senha = sys.argv[2]
#         i = 1
# opcao = sys.argv[2+i]
# if verificadorOpcao(opcao) == -1:
#     print("Parâmetro <opção> inválido!")
# pasta = sys.argv[3+i]
# if verificadorPasta(pasta)== -1:
#     print("Parâmetro <pasta> inválido!")
# try:
#     saida = sys.argv[4+i]
# except:
#     saida = None
#     pass

print("========= Configuração ============")
print("Método: " +  metodo)
if metodo == "hmac":
    print("Senha: " + senha)
print("Opção: " + opcao)
print("Pasta: " + pasta)
print("Arquivo de saída: " + saida)
print("===================================")
files = []
for r, d, f in os.walk(pasta):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    print(f)