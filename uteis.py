stringTitulo = 'Bem vindo a MV.ARLINES.\nSua melhor opção para viajar o Brasil.\nRealize seu cadastro ou entre na sua conta!'

def escreveArquivoViagens():
    with open('viagens.csv', 'w') as f:
        f.write("Partida:São Paulo,Destino:Manaus,HoraPartida:18h22m,HoraChegada:20h47m,DataPartida:12/06/2019,DataChegada:12/06/2019,Voo:87JK,Preço:836.03;\n\
Partida:São Paulo,Destino:Rio de Janeiro,HoraPartida:23h41m,HoraChegada:01h28m,DataPartida:12/06/2019,DataChegada:13/06/2019,Voo:AI1O,Preço:421.30;\n\
Partida:São Paulo,Destino:Fortaleza,HoraPartida:13h02m,HoraChegada:17h10m,DataPartida:14/07/2019,DataChegada:14/07/2019,Voo:JS52,Preço:727.41;\n\
Partida:São Paulo,Destino:Porto Alegre,HoraPartida:21h22m,HoraChegada:23h10m,DataPartida:13/07/2019,DataChegada:13/07/2019,Voo:JS53,Preço:622.45;\n\
Partida:São Paulo,Destino:Salvador,HoraPartida:05h10m,HoraChegada:08h29m,DataPartida:13/07/2019,DataChegada:13/07/2019,Voo:OI19,Preço:722.45;\n\
Partida:Salvador,Destino:Manaus,HoraPartida:12h34m,HoraChegada:14h49m,DataPartida:12/06/2019,DataChegada:12/06/2019,Voo:ABW2,Preço:836.03;\n\
Partida:Salvador,Destino:Rio de Janeiro,HoraPartida:03h27m,HoraChegada:06h29m,DataPartida:12/06/2019,DataChegada:13/06/2019,Voo:AQ14,Preço:421.30;\n\
Partida:Salvador,Destino:Fortaleza,HoraPartida:13h02m,HoraChegada:17h10m,DataPartida:14/07/2019,DataChegada:14/07/2019,Voo:LA29,Preço:727.41;\n\
Partida:Salvador,Destino:Porto Alegre,HoraPartida:21h22m,HoraChegada:23h10m,DataPartida:13/07/2019,DataChegada:13/07/2019,Voo:0OPL,Preço:622.45;\n\
Partida:Salvador,Destino:São Paulo,HoraPartida:05h10m,HoraChegada:08h26m,DataPartida:13/07/2019,DataChegada:13/07/2019,Voo:1AKI,Preço:722.45;\n\
Partida:São Paulo,Destino:Miami,HoraPartida:05h40m,HoraChegada:00h10m,DataPartida:13/07/2019,DataChegada:14/07/2019,Voo:QNX2,Preço:1512.24;\n\
Partida:Manaus,Destino:Miami,HoraPartida:02h25m,HoraChegada:23h17m,DataPartida:14/07/2019,DataChegada:14/07/2019,Voo:D23P,Preço:1422.45;\n\
Partida:Manaus,Destino:Rio de Janeiro,HoraPartida:02h48m,HoraChegada:03h10m,DataPartida:14/07/2019,DataChegada:14/07/2019,Voo:AWS1,Preço:836.03;\n\
Partida:Manaus,Destino:Fortaleza,HoraPartida:21h22m,HoraChegada:00h26m,DataPartida:14/07/2019,DataChegada:15/07/2019,Voo:QXZ4,Preço:930.23;\n\
Partida:Manaus,Destino:Porto Alegre,HoraPartida:23h41m,HoraChegada:04h23m,DataPartida:15/07/2019,DataChegada:16/07/2019,Voo:ZWRT,Preço:930.23;\n\
Partida:Manaus,Destino:São Paulo,HoraPartida:12h34m,HoraChegada:15h21m,DataPartida:15/07/2019,DataChegada:15/07/2019,Voo:15AQ,Preço:842.34;\n\
Partida:Manaus,Destino:Salvador,HoraPartida:19h25m,HoraChegada:21h12m,DataPartida:14/07/2019,DataChegada:14/07/2019,Voo:45PQ,Preço:590.90;\n\
Partida:Porto Alegre,Destino:Salvador,HoraPartida:18h22m,HoraChegada:20h47m,DataPartida:14/07/2019,DataChegada:14/07/2019,Voo:WTY2,Preço:580.20;\n\
Partida:Porto Alegre,Destino:Manaus,HoraPartida:05h10m,HoraChegada:11h47m,DataPartida:15/07/2019,DataChegada:16/07/2019,Voo:QATE,Preço:899.23;\n\
Partida:Porto Alegre,Destino:Rio de Janeiro,HoraPartida:12h34m,HoraChegada:15h45m,DataPartida:15/07/2019,DataChegada:15/07/2019,Voo:TYU3,Preço:423.78;\n\
Partida:Porto Alegre,Destino:Fortaleza,HoraPartida:22h34m,HoraChegada:02h00m,DataPartida:15/07/2019,DataChegada:16/07/2019,Voo:YUA1,Preço:950.29;\n\
Partida:Porto Alegre,Destino:São Paulo,HoraPartida:12h34m,HoraChegada:13h57m,DataPartida:16/07/2019,DataChegada:16/07/2019,Voo:234J,Preço:834.21;\n\
Partida:Rio de Janeiro,Destino:Salvador,HoraPartida:23h41m,HoraChegada:00h45m,DataPartida:16/07/2019,DataChegada:17/07/2019,Voo:14GH,Preço:790.02;\n\
Partida:Rio de Janeiro,Destino:Manaus,HoraPartida:15h23m,HoraChegada:17h57m,DataPartida:16/07/2019,DataChegada:16/07/2019,Voo:78DH,Preço:799.34;\n\
Partida:Rio de Janeiro,Destino:Fortaleza,HoraPartida:21h53m,HoraChegada:01h00m,DataPartida:16/07/2019,DataChegada:17/07/2019,Voo:IUH3,Preço:901.02;\n\
Partida:Rio de Janeiro,Destino:São Paulo,HoraPartida:20h02m,HoraChegada:21h45m,DataPartida:16/07/2019,DataChegada:16/07/2019,Voo:14AK,Preço:400.32;")

def imprimeTitulo():
    print('\33[94m' + '--'*45)
    print(stringTitulo)
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
        print('')
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
        print('')
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