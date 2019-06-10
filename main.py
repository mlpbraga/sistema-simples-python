#teste 1 - Empresa Area
from usuarios import *
from viagens import *
from uteis import *

def main(viagens):
    arquivoUsr = open('person.csv', 'a+')
    arquivoUsr.close()
    imprimeTitulo()
    o_que_fazer = imprimeMenuInicial()
    usr = Usuario()

    if o_que_fazer == 1:
        o_que_fazer = usr.cadastrar()

    if o_que_fazer == 2:
        retry = 'S'
        while retry in ['S', 's', 'sim']:
            print('\n\33[94m> Preencha os dados de login.')
            username = input('>> Usuario: ')
            password = input('>> Senha: ')
            resultado = usr.entrar(username,password)
            if resultado == None:
                retry = input("\n\33[94m> Deseja tentar novamente?(S/n): ")
            else:
                retry = 'x'
    
        while resultado:
            to_do = imprimeMenuPrincipal()
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
            elif to_do == 4:
                usr.imprimirViagens(False)
                if imprimirMenuMinhasViagens() == 1:
                    print("\33[94m> Qual voo você deseja remover?")
                    remover = input('\33[0m ::')
                    usr.removerViagem(remover)
                    usr.imprimirViagens()
            elif to_do == 5:
                print('\33[94m> Até a próxima,', usr.dados['Nome'],':).')
                return None

escreveArquivoViagens()
via = Viagens()
main(via)