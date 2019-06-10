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

class Viagens:
    def __init__(self, arquivo='viagens.csv'):
        self.lista = []

        with open(arquivo, 'r+') as f:
            dados = f.readlines()
            viagem = dict()
            for dado in dados:
                atributos = dado.strip(';').split(',')
                for atributo in atributos:
                    chave_valor = atributo.split(':')
                    if chave_valor[0] == 'Preço':
                        viagem[chave_valor[0]] = float(chave_valor[1].strip(';\n'))
                    else:
                        viagem[chave_valor[0]] = chave_valor[1]
                self.lista.append(viagem)
                viagem = dict()

    def listarTodas(self, menuCompras=True):
        if len(self.lista) > 0:
            for elemento in self.lista:
                imprimeDicionario(elemento)
            if menuCompras:
                return imprimeMenuDeCompra()
        else:
            print('\33[95m> Não existem viagens correspondentes a essa consulta :/.\33[94m')
            return None

    def precoMenorQue(self, limite):
        print('\33[94m> Passagens com valor menor que \33[23mR$ ' + str(limite) + '\33[94m')
        for elemento in self.lista:
            if elemento.get('Preço') <= limite:
                imprimeDicionario(elemento)
        return imprimeMenuDeCompra()

    def partidaDestino(self, partida, destino):
        print('\33[94m> Passagens que saem de \33[93m' + partida + ' e vão até ' + destino + '\33[94m')
        for elemento in self.lista:
            if elemento.get('Partida') == partida and elemento.get('Destino') == destino:
                imprimeDicionario(elemento)
        return imprimeMenuDeCompra()

    def getVoo(self, voo):
        for elemento in self.lista:
            if elemento.get('Voo') == voo:
                return elemento