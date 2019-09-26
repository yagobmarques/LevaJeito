import sys
import os
def verificadorMetodo(metodo): # Função que retorna -1 se a entrada do método é inválida, 1 se é -hash e 2 se é -hmac
    if metodo == "-hash":
        return 1
    if metodo == "-hmac":
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

# Pegando arqumentos passados pelo usuário
i = 0 # Contador auxiliar
metodo = sys.argv[1]
if verificadorMetodo(metodo) == -1:
    print("Parâmetro <método> inválido!")
else:
    if verificadorMetodo(metodo)==2:
        senha = sys.argv[2]
        i = 1
opcao = sys.argv[2+i]
if verificadorOpcao(opcao) == -1:
    print("Parâmetro <opção> inválido!")
pasta = sys.argv[3+i]
if verificadorPasta(pasta)== -1:
    print("Parâmetro <pasta> inválido!")
try:
    saida = sys.argv[4+i]
except:
    saida = None
    pass
print("========= Configuração ============")
print("Método: " +  metodo)
if metodo == "-hmac":
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