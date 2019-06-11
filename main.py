#teste 1 - Empresa Area
from usuarios import *
from viagens import *
from uteis import *

# a função main mantem os menus funcionando até que o usuário 
# deseje sair e inicializa todos os arquivos e valores necessários.

def main(viagens):
    arquivoUsr = open('person.csv', 'a+')
    arquivoUsr.close()
    imprimeTitulo()
    
    # a função imprimeMenuInicial recebe valores 1 ou 2
    o_que_fazer = imprimeMenuInicial()
    usr = Usuario()

    # caso o valor seja 1, o sistema cadastra um novo usuário
    if o_que_fazer == 1:
        o_que_fazer = usr.cadastrar()

    # caso o valor seja 2, o sistema pede o usuário e a senha da pessoa
    if o_que_fazer == 2:
        retry = 'S'
        while retry in ['S', 's', 'sim']:
            print('\n\33[94m> Preencha os dados de login.')
            username = input('>> Usuario: ')
            password = input('>> Senha: ') 
            resultado = usr.entrar(username,password)

            # se o usuário e a senha são invalidos, o usuário pode tentar novamente
            if resultado == None:
                retry = input("\n\33[94m> Deseja tentar novamente?(S/n): ")
            # se o usuário e a senha são válidos então passamos pro poximo menu            
            else:
                retry = 'x'
    
        while resultado:
            # recebe a opção do que o usuario quer fazer no menu principal
            to_do = imprimeMenuPrincipal()
            
            # se ele digitar 1, ele irá ver todos os voos disponíveis para compra 
            if to_do == 1:
                comprar = viagens.listarTodas(True)
                if comprar == 1:
                    print("\33[94m> Qual o ID do Voo que você deseja comprar?")
                    voou = input('\33[0m:: ')
                    pega = viagens.getVoo(voou)
                    if pega == False:
                        print('\n\33[95m> Esse código é inválido...\33[94m') 
                    else: 
                        usr.inserirViagem(pega)

            # se ele digitar 2, o programa pede que ele digite o preço máximo
            # para os voos que ele irá mostrar, e então é exibida uma lista com
            # os voos que atendem a condição de preço
            elif to_do == 2: 
                print("\33[94m> Qual o preço máximo das passagens que devo te mostrar?")
                limite = float(input('\33[0m:: R$ '))
                comprar = viagens.precoMenorQue(limite)
                if comprar == 1:
                    print("\33[94m> Qual o ID do Voo que você deseja comprar?")
                    voou = input('\33[0m ::')
                    pega = viagens.getVoo(voou)
                    if pega == False:
                        print('\n\33[95m> Esse código é inválido...\33[94m') 
                    else: 
                        usr.inserirViagem(pega)

            # se ele digitar 3, o programa pede para saber qual o local de partida
            # e o destino do usuário, e então o programa só exibirá os voos que atendem
            # a consulta do usuário
            elif to_do == 3:
                print("\33[94m> Qual seu destino?")
                destino = input('\33[0m ::')
                print("\33[94m> Qual o local de partida?")
                partida = input('\33[0m ::')
                comprar = viagens.partidaDestino(partida,destino)
                if comprar == 1:
                    print("\33[94m> Qual o ID do Voo que você deseja comprar?")
                    voou = input('\33[0m ::')
                    pega = viagens.getVoo(voou)
                    if pega == False:
                        print('\n\33[95m> Esse código é inválido...\33[94m') 
                    else: 
                        usr.inserirViagem(pega)
            
            # se ele digitar 4, o programa exibe uma lista com todas as viagens 
            # que estão programadas para esse usuário
            elif to_do == 4:
                usr.imprimirViagens(False)
                if imprimirMenuMinhasViagens() == 1:
                    print("\33[94m> Qual voo você deseja remover?")
                    remover = input('\33[0m ::')
                    usr.removerViagem(remover)
                    usr.imprimirViagens()
            
            # se ele digitar 5, o programa é fechado.
            elif to_do == 5:
                print('\33[94m> Até a próxima,', usr.dados['Nome'],':).')
                return None

escreveArquivoViagens()
via = Viagens()
main(via)