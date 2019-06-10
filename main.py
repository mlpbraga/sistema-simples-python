#teste 1 - Empresa Area
from usuarios import *
from viagens import *
from uteis import *

def main(viagens):
    imprimeTitulo()
    o_que_fazer = imprimeMenuInicial()
    usr = Usuario()

    if o_que_fazer == 1:
        o_que_fazer = usr.cadastrar()

    if o_que_fazer == 2:
        retry = 'S'
        while retry in ['S', 's', 'sim']:
            print('\33[94m> Preencha os dados de login.')
            username = input('>> Usuario: ')
            password = input('>> Senha: ')
            resultado = usr.entrar(username,password)
            if resultado == None:
                retry = input("\33[94m> Deseja tentar novamente?(S/n): ")
            else:
                retry = 'x'
    
        while resultado:
            to_do = imprimeMenuPrincipal()
            if to_do == 1:
                comprar = viagens.listarTodas()
                if comprar == 1:
                    print("\33[94m> Qual o ID do Voo que você deseja comprar?")
                    voou = input(':: ')
                    pega = viagens.getVoo(voou)
                    usr.inserirViagem(pega)
            elif to_do == 2: 
                print("\33[94m> Qual o preço máximo das passagens que devo te mostrar?")
                limite = float(input(':: R$ '))
                comprar = viagens.precoMenorQue(limite)
                if comprar == 1:
                    print("\33[94m> Qual o ID do Voo que você deseja comprar?")
                    voou = input(':: ')
                    pega = viagens.getVoo(voou)
                    usr.inserirViagem(pega)
            elif to_do == 3:
                print("\33[94m> Qual seu destino?")
                destino = input(':: ')
                print("\33[94m> Qual o local de partida?")
                partida = input(':: ')
                comprar = viagens.partidaDestino(partida,destino)
                if comprar == 1:
                    print("\33[94m> Qual o ID do Voo que você deseja comprar?")
                    voou = input(':: ')
                    pega = viagens.getVoo(voou)
                    usr.inserirViagem(pega)
            elif to_do == 4:
                usr.imprimirViagens(False)
                if imprimirMenuMinhasViagens() == 1:
                    print("\33[94m> Qual voo você deseja remover?")
                    remover = input(':: ')
                    usr.removerViagem(remover)
                    usr.imprimirViagens()
            elif to_do == 5:
                print('\33[94m> Até a próxima,', usr.dados['Nome'],':).')
                return None

via = Viagens()
escreveArquivoViagens()
main(via)