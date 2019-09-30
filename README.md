# Operação Leva Jeito

## Linguagem
Python 3.7.4
## Contribuidor
Yago Beserra Marques
## Como usar
``./guarda < metodo > < opcao> < pasta > < saída >``  

- método : indica o método a ser utilizado ( -hash ou -hmac senha)

- opção: indica a ação a ser desempenhada pelo programa
    - -i: inicia a guarda da pasta indicada em <pasta>, ou seja, faz a leitura de todos os arquivos da pasta (recursivamente)
registrando os dados e Hash/HMAC de cada um e armazenando numa estrutura própria.
    - -t : faz o rastreio (tracking) da pasta indicada em <pasta>, inserindo informações sobre novos arquivos e indicando
alterações detectadas/exclusões
    - -x: indica a pasta a ser “guardada”

- pasta: indica a pasta a ser “guardada

- saida: indica o arquivo de saída para o relatório (-o saída). Caso não seja passado este parâmetro saída deve ser feita em tela.(opcional)  
