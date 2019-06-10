def escreveArquivoViagens():
    with open('viagens.csv', 'w') as f:
        f.write('Partida:São Paulo,Destino:Manaus,HoraPartida:18h32m,HoraChegada:20h47m,DataPartida:12/06/2019,DataChegada:12/06/2019,Voo:87JK,Preço:836.03;\n')
        f.write('Partida:Manaus,Destino:São Paulo,HoraPartida:03h21m,HoraChegada:05h45m,DataPartida:13/06/2019,DataChegada:13/06/2019,Voo:70AB,Preço:832.24;\n')
        f.write('Partida:Manaus,Destino:Rio Grande do Sul,HoraPartida:12h49m,HoraChegada:17h423m,DataPartida:14/06/2019,DataChegada:14/06/2019,Voo:93J1,Preço:952.31;\n')

def imprimeTitulo():
    print('\33[94m' + '--'*45)
    print('Bem vindo a MV.ARLINES.')
    print('Sua melhor opção para viajar o Brasil.')
    print('Realize seu cadastro ou entre na sua conta!')
    print('--'*45 + '\33[0m')

def imprimeDicionario(dicionario):
    print('\33[93m' + '-'*90)
    print('Voo: ' + dicionario.get('Voo') + '\t\t\t\33[92m Preço: R$' + str(dicionario['Preço']) + '\33[93m')
    print('Data de ida: ' + dicionario['DataPartida'] + '\t\t Data de chegada:' + dicionario['DataChegada'])
    print('Horário da ida: ' + dicionario['HoraPartida'] + '\t\t Horário da chegada:' + dicionario['HoraChegada'])
    print('Local de partida: ' + dicionario['Partida'] + '\t Local de destino: ' + dicionario['Destino'])

def imprimeMenuDeCompra():
    print('\33[94m' + '--'*45)
    print('1 - Comprar uma passagem')
    print('2 - Voltar para o menu principal')
    while True:
        entrada = input('\33[97m:: ')
        if entrada.lower() in ['1', 'comprar']:
            return 1
        elif entrada.lower() in ['2', 'voltar']:
            return 2
        print('\33[95m> Opção inválida, procure inserir uma das opções listadas no menu.\33[94m')
        print('\33[94m' + '--'*45)
        print('1 - Comprar uma passagem')
        print('2 - Voltar para o menu principal')


def imprimeMenuInicial():
    print('\33[94m' + '--'*19 + ' MENU INICIAL ' + '--'*19)
    print('1 - Cadastrar uma conta')
    print('2 - Entrar na minha conta')

    while True:
        entrada = input('\33[97m:: ')
        if entrada.lower() in ['1', 'cadastrar', 'cadastrar uma conta']:
            return 1
        elif entrada.lower() in ['2', 'entrar', 'entrar na minha conta']:
            return 2
        print('\33[95m> Opção inválida, procure inserir uma das opções listadas no menu.\33[94m')
        print('\33[94m' + '--'*19 + ' MENU INICIAL ' + '--'*19)
        print('1 - Cadastrar uma conta')
        print('2 - Entrar na minha conta')       

def imprimeMenuPrincipal():
    print('\33[94m' + '--'*18 + '- MENU PRINCIPAL -' + '--'*18)
    print('1 - Listar todas as viagens')
    print('2 - Pesquisar passagens por preço')
    print('3 - Pesquisar por locais e partida e destino')
    print('4 - Listar minhas viagens')
    print('5 - Sair')

    while True:
        entrada = input('\33[97m:: ')
        if entrada.lower() in ['1', 'todas', 'listar todas as viagens']:
            return 1
        elif entrada.lower() in ['2', 'preço', 'listar viagens com melhor preço']:
            return 2
        elif entrada.lower() in ['3', 'destino', 'partida']:
            return 3
        elif entrada.lower() in ['4', 'minhas viagens', 'listar minhas viagens']:
            return 4
        elif entrada.lower() in ['5', 'sair']:
            return 5
        print('\33[95m> Opção inválida, procure inserir uma das opções listadas no menu.\33[94m')
        print('\33[94m' + '--'*18 + '- MENU PRINCIPAL -' + '--'*18)
        print('1 - Listar todas as viagens')
        print('2 - Pesquisar passagens por preço')
        print('3 - Pesquisar por locais e partida e destino')
        print('4 - Listar minhas viagens')
        print('5 - Sair')

def imprimirMenuMinhasViagens():
    print('\33[94m' + '--'*18 + '- MINHAS VIAGENS -' + '--'*18)
    print('1 - Remover viagem')
    print('2 - Voltar para o menu principal')

    while True:
        entrada = input('\33[97m:: ')
        if entrada.lower() in ['1', 'remover']:
            return 1
        elif entrada.lower() in ['2', 'voltar']:
            return 2
  
        print('\33[95m> Opção inválida, procure inserir uma das opções listadas no menu.\33[94m')
        print('\33[94m' + '--'*18 + '- MINHAS VIAGENS -' + '--'*18)
        print('1 - Remover viagem')
        print('2 - Voltar para o menu principal')