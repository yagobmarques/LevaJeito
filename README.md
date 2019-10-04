# Operação Leva Jeito

## Linguagem
Python 3.7.4
## Contribuidor
Yago Beserra Marques
## Como usar
``` python3 ./guarda < metodo > < opcao> < pasta > < saída >```  

* <método>: indica o método a ser utilizado ( -hash ou -hmac senha)
* <pasta>: indica a pasta a ser “guardada
* <saida>: indica o arquivo de saída para o relatório (-o saída). Caso não seja passado este parâmetro saída deve ser feita em tela.(opcional) 
* <opção>: indica a ação a ser desempenhada pelo programa
    * -i: inicia a guarda da pasta indicada em <pasta>, ou seja, faz a leitura de todos os arquivos da pasta (recursivamente)
registrando os dados e Hash/HMAC de cada um e armazenando numa estrutura própria.
    * -t : faz o rastreio (tracking) da pasta indicada em <pasta>, inserindo informações sobre novos arquivos e indicando
alterações detectadas/exclusões
    * -x:  desativa a guarda e remove a estrutura alocada

 
## Descrição do programa
Ao começar a monitorar uma pasta, a mesma faz uma varredura de todos os arquivos abaixo dessa pasta, gerando a hash de cada um deles e salvando em um arquivo oculto .guarda o formato "<filename> > <hash>". Assim, ao iniciar o "tracking" (opção -t), é feita uma nova varredura e os hash's são comparados com os do arquivo .guarda, gerando assim 4 status para o cada arquivo (novo, excluido, normal, alterado). Por fim, a opção -x apenas apaga o arquivo .guarda e joga no output em questão se fora bem sucedido ou não.
## Execução do programa
    * Iniciando a varredura
![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Iniciando%20a%20varredura.png)
    * Bilbo:
    
