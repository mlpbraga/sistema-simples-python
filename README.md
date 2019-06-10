# sistema-simples-python
Trabalho de LP1

O trabalho implementa um sistema simples de consulta de preços e compras de passagens.

O sistema consiste em 3 arquivos: 
* `main.py`  - arquivo com o loop de repetição que executa as funções de menu
* `usuarios.py` - arquivo com implementações de uma classe para um usuário do sistema
* `viagens.py` - arquivo com implementações de uma classe para as viagens de usuário ou do sistema inteiro

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

