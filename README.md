# Operação Leva Jeito

## Linguagem
Python 3.7.4
## Contribuidor
Yago Beserra Marques
## Como usar
``` python3 ./guarda < metodo > < opcao > < pasta > < saída >```  
* < metodo >: indica o método a ser utilizado ( -hash ou -hmac senha)
* < pasta >: indica a pasta a ser "guardada"
* < saida >: indica o arquivo de saída para o relatório (-o saída). Caso não seja passado este parâmetro saída deve ser feita em tela.(opcional) 
* < opcao >: indica a ação a ser desempenhada pelo programa
    * -i: inicia a guarda da pasta indicada em <pasta>, ou seja, faz a leitura de todos os arquivos da pasta (recursivamente)
registrando os dados e Hash/HMAC de cada um e armazenando numa estrutura própria.
    * -t : faz o rastreio (tracking) da pasta indicada em <pasta>, inserindo informações sobre novos arquivos e indicando
alterações detectadas/exclusões
    * -x:  desativa a guarda e remove a estrutura alocada

 
## Descrição do programa
Ao começar a monitorar uma pasta, a mesma faz uma varredura de todos os arquivos abaixo dessa pasta, gerando a hash de cada um deles e salvando em um arquivo oculto .guarda o formato "<filename> > <hash>". Assim, ao iniciar o "tracking" (opção -t), é feita uma nova varredura e os hash's são comparados com os do arquivo .guarda, gerando assim 4 status para o cada arquivo (novo, excluido, normal, alterado). Por fim, a opção -x apenas apaga o arquivo .guarda e joga no output em questão se fora bem sucedido ou não.
## Execução do programa
* Iniciando a varredura:
   
![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Iniciando%20a%20varredura.png)

* Less arquivo de saida da varredura:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Less%20arq_saida%20-%20Varredura.png)

* Tracking da pasta:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Tracking.png)

* Less arquivo de saida do tracking:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Less%20tracking.png)

* Adicionando um arquivo e re-fazendo o tracking:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Criando%20um%20arquivo%20e%20fazendo%20tracking.png)

* Less arquivo de saida do tracking:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Less%20arq_saida%20-%20Apos%20adicionar%20arquivoi.png)

* Removendo um arquivo e re-fazendo o tracking:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Removendo%20um%20arquivo%20e%20fazendo%20a%20tracking.png)

* Saida após remover o arquivo:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Saida%20apos%20remover%20Funçoes%20hash.png)

* Tracking na saida padrão:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Saida%20padrao.png)

* Removendo o monitoramento de uma pasta:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/removendo%20o%20monitoramento%20de%20uma%20pasta.png)

* Tentando remover uma pasta que não está sendo monitorada:

![alt text](https://raw.githubusercontent.com/yagobmarques/LevaJeito/master/Fotos%20Programa/Removendo%20uma%20pasta%20que%20n~ao%20est'a%20sendo%20monitorada.png)
