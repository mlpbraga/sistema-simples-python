# Sistema de Exibição e Controle de Passagens

O trabalho implementa um sistema simples de consulta de preços e compras de passagens.

**Dependências:**
- [Python3](https://www.python.org/downloads/)
- [Kivy](https://kivy.org/#home)

# Como rodar?
```sh
$ python3 app.py # com telas
$ python3 main.py # no terminal
```

# Disposição de arquivos
O sistema principalmente nos arquivos:
* `uteis.py` - arquivo com funções uteis durante a execução do programa, principalmente para melhorar a interface
* `main.py`  - arquivo com o loop de repetição que executa as funções de menu
* `viagens.py` - arquivo com implementações de uma classe para as viagens de usuário ou do sistema inteiro
* `usuarios.py` - arquivo com implementações de uma classe para um usuário do sistema
* `app.py` - arquivo com a implementação e uso de telas

## Arquivo app.py
Esse arquivo contém todas as telas usadas no sistema. Cada classe escrita aqui tem um `.kv` que define a apresentação dos componentes nas telas.

## Arquivo main.py
Esse arquivo contém toda a lógica de repetição e continuidade das exibições de menu e acesso ao sistema. Nele existe uma função chamada `main()` que, dependendo das respostas do usuário, decide o que será feito no programa.
Ao fim desse arquivo, temos a criação do objeto de viagens, a escrita do arquivo que contém todas as viagens possíveis para o usuário e a chamada da função main.

**De onde eu tirei as cores do terminal?**
https://github.com/mlpbraga/utils/blob/master/terminal-colors.md
