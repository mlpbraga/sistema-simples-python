# Sistema de Exibição e Controle de Passagens
Trabalho de LP1

O trabalho implementa um sistema simples de consulta de preços e compras de passagens.

O sistema consiste em 4 arquivos:
* `uteis.py` - arquivo com funções uteis durante a execução do programa, principalmente para melhorar a interface
* `main.py`  - arquivo com o loop de repetição que executa as funções de menu
* `viagens.py` - arquivo com implementações de uma classe para as viagens de usuário ou do sistema inteiro
* `usuarios.py` - arquivo com implementações de uma classe para um usuário do sistema

## Arquivo main.py
Esse arquivo contém toda a lógica de repetição e continuidade das exibições de menu e acesso ao sistema. Nele existe uma função chamada `main()` que, dependendo das respostas do usuário, decide o que será feito no programa.
Ao fim desse arquivo, temos a criação do objeto de viagens, a escrita do arquivo que contém todas as viagens possíveis para o usuário e a chamada da função main.

## Arquivo uteis.py
Esse arquivo engloba diversas funções utilizadas ao longo do programa, são elas:

- `escreveArquivoViagens()` : essa função foi criada para criar o arquivo com todas as viagens que estarão disponíveis no sistema para o usuário, ela abre o arquivo `viagens.csv` e insere nele todas as viagens possíveis. Essa função não deve imprimir nada na tela.

- `imprimeTitulo()` : essa função foi criada para exibir a mensagem de boas vindas quando o programa abre, quando chamada ela imprime a seguinte mensagem:

```
------------------------------------------------------------------------------------------
Bem vindo a MV.ARLINES.
Sua melhor opção para viajar o Brasil.
Realize seu cadastro ou entre na sua conta!
------------------------------------------------------------------------------------------
```

- `imprimeDicionario(dicionario)` : foi criada para imprimir dicionários referentes as viagens, passando uma viagem como parâmetro para essa função, temos uma saída no formato abaixo, que representa uma viagem cuja passagem pode ser comprada pelo usuário:
```
------------------------------------------------------------------------------------------
Voo: 87JK                        Preço: R$836.03
Data de ida: 12/06/2019          Data de chegada:12/06/2019
Horário da ida: 18h32m           Horário da chegada:20h47m
Local de partida: São Paulo      Local de destino: Manaus
```

- `imprimeMenuDeCompra()` : foi criada pra imprimir o menu exibido abaixo e questionar se o usuário tem o desejo de comprar uma passagem em um dos voos listados ou não:

```
------------------------------------------------------------------------------------------
1 - Comprar uma passagem
2 - Voltar para o menu principal
```

- `imprimeMenuInicial()` : essa função exibe as opções do menu inicial do programa e recebe o tipo de operação que o usuário deseja realizar, a mensagem que essa função exibe na tela é como a mensagem abaixo:

```
-------------------------------------- MENU INICIAL --------------------------------------
1 - Cadastrar uma conta
2 - Entrar na minha conta
```

- `imprimeMenuPrincipal()` : essa função exibe as opções do menu principal do programa e recebe o tipo de operaçao que o usuário deseja realizar, a mensagem que essa função exibe na tela é como a mensagem abaixo:
```
------------------------------------- MENU PRINCIPAL -------------------------------------
1 - Listar todas as viagens
2 - Pesquisar passagens por preço
3 - Pesquisar por locais e partida e destino
4 - Listar minhas viagens
5 - Sair
```

- `imprimirMenuMinhasViagens()` :  essa função exibe as opções do menu "minhas viagens" do usuário, a mensagem exibida por essa função deve ser como a mensagem abaixo:

```
------------------------------------- MINHAS VIAGENS -------------------------------------
1 - Remover viagem
2 - Voltar para o menu principal
```

## Classe Viagens
Consiste em um objeto que possui uma lista de dicionários, onde cada dicionário corresponde a uma viagem cadastrada no início do programa. As viagens cadastradas são armazenadas no arquivo `viagens.csv`. Abaixo, segue um exemplo do dicionário que representa uma viagem:

```json
{
  "Partida": "São Paulo",
  "Destino": "Manaus",
  "HoraPartida": "18h32m",
  "HoraChegada": "20h47m",
  "DataPartida": "12/06/2019",
  "DataChegada": "12/06/2019",
  "Voo": "87JK",
  "Preço": 836.03
}
```
**Métodos da classe Viagens:**

- `listarTodas()` : lista de forma amigável todas as viagens cadastradas no início do programa e armazenadas em `viagens.csv`.

- `precoMenorQue(limite)` : lista todas as viagens que estão cadastradas no sistema **e** tem um preço abaixo do `limite` passado como parâmetro.

- `partidaDestino(partida, destino)` : lista todas as viagens que estão cadastradas no sistema **e** partem do parâmetro passado como `partida` e chegam no parâmetro passado como `destino`.

- `getVoo(voo)` : pega todas as informações de uma viagem para o código do Voo passado como parâmetro.


## Classe Usuario
Consistem em um objeto que possui um dicionário que guarda todas as informações de um Usuário. Todos os usuários são escritos em um arquivo chamado `person.csv`. Abaixo, segue um exemplo do dicionário que representa um usuário

```json
{
  "Usuario": "vinipalheta",
  "Senha": "1234",
  "Nome": "Vinicius Palheta",
  "Idade": "15",
  "CPF": "1831927381721",
  "Email": "vinipalheta@gmail.com",
  "Telefone": "12324312",
  "Endereço": "Rua 1, Casa 1, Bairro 2"
}
        
```
**Métodos da classe Usuario:**

- `cadastrar()` : recolhe os dados de um usuário que deseja se cadastrar e cria um novo usuário adicionando no arquivo `person.csv` um novo usuário e adicionando um arquivo `viagens-{username}.csv` onde serão escritas todas as viagens que aquele usuário cadastrou.

- `entrar(usuario, senha)` : recebe um usuário e uma senha e retorna o objeto equivalente a um usuário caso a o usuário e a senha passados como parâmetro sejam correspondentes a um usuário já cadastrado. Caso os valores passados sejam inválidos, o método retorna nulo.

- `inserirViagem(viagem)` : insere uma viagem na lista de compras para o usuário em questão, adicionando os dados dessa viagem no arquivo `viagens-{username}.csv`.

- `removerViagem(voo)` : usa o ID de um voo para removê-lo da lista de viagens escrita no arquivo `viagens-{username}.csv`.

- `imprimirViagens(menuCompras=False)` : imprime todas as viagens do usuário que estão escritas no arquivo `viagens-{username}.csv`.

