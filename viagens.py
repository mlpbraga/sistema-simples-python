from uteis import *


class Viagens:
    def __init__(self, arquivo='csv/viagens.csv'):
        self.lista = []

        with open(arquivo, 'r+') as f:
            dados = f.readlines()
            viagem = dict()
            for dado in dados:
                atributos = dado.strip(';').split(',')
                for atributo in atributos:
                    chave_valor = atributo.split(':')
                    if chave_valor[0] == 'Preço':
                        viagem[chave_valor[0]] = float(
                            chave_valor[1].strip(';\n'))
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
            print(
                '\33[95m> Não existem viagens correspondentes a essa consulta :/.\33[94m')
            return None

    def precoMenorQue(self, limite):
        tinha = False
        print('\33[94m> Passagens com valor menor ou igual a \33[23mR$ ' +
              str(limite) + '\33[94m')
        for elemento in self.lista:
            if elemento.get('Preço') <= limite:
                imprimeDicionario(elemento)
                tinha = True
        if tinha:
            return imprimeMenuDeCompra()
        elif not tinha:
            print(
                '\33[95m> Não existem viagens correspondentes a essa consulta :/.\33[94m')
            return None

    def partidaDestino(self, partida, destino):
        tinha = False
        print('\33[94m> Passagens que saem de \33[93m' +
              partida + ' e vão até ' + destino + '\33[94m')
        for elemento in self.lista:
            if elemento.get('Partida').lower() == partida.lower() and elemento.get('Destino').lower() == destino.lower():
                imprimeDicionario(elemento)
                tinha = True
        if tinha:
            return imprimeMenuDeCompra()
        elif not tinha:
            print(
                '\33[95m> Não existem viagens correspondentes a essa consulta :/.\33[94m')
            return None

    def getVoo(self, voo):
        for elemento in self.lista:
            if elemento.get('Voo').lower() == voo.lower():
                return elemento
        return False

    def mostrarTodas(self):
        palavras = ''
        palavras += '\nListagem de todas as viagens disponíveis'
        if len(self.lista) > 0:
            for elemento in self.lista:
                palavras += '\n' + '-'*90
                palavras += '\nVoo: ' + elemento.get('Voo') + ' Preço: R$' + str(
                    elemento['Preço']) + '\nLocal de partida: ' + elemento['Partida'] + ' |  Local de destino: ' + elemento['Destino']
                palavras += '\nData de ida: ' + elemento['DataPartida'] + ' |  Horário da ida: ' + elemento['HoraPartida'] + \
                    '\nData de chegada: ' + \
                    elemento['DataChegada'] + \
                    ' | Horário da chegada: ' + elemento['HoraChegada']
        else: 
            palavras = 'Não tem nada aqui :/'
        return palavras

    def mostrarPrecoMenor(self, limite):
        palavras = ''
        palavras += '\nListagem de todas as viagens disponíveis com preço menor que R$ {}'.format(
            limite)
        print('\33[94m> Passagens com valor menor ou igual a \33[23mR$ ' +
              str(limite) + '\33[94m')
        if len(self.lista) > 0:
            for elemento in self.lista:
                if elemento.get('Preço') <= limite:
                    palavras += '\n' + '-'*90
                    palavras += '\nVoo: ' + elemento.get('Voo') + ' Preço: R$' + str(
                        elemento['Preço']) + '\nLocal de partida: ' + elemento['Partida'] + ' |  Local de destino: ' + elemento['Destino']
                    palavras += '\nData de ida: ' + elemento['DataPartida'] + ' |  Horário da ida: ' + elemento['HoraPartida'] + \
                        '\nData de chegada: ' + \
                        elemento['DataChegada'] + \
                        ' | Horário da chegada: ' + elemento['HoraChegada']
        else:
            palavras += '\n' + '-'*90
            palavras += 'Não encontrei resultados para essa consulta :c'

        return palavras

    def mostrarPartidaDestino(self, partida, destino):
        palavras = ''
        palavras += 'Listagem de todas as viagens disponíveis que saem de {0} e vão até {1}'.format(
            partida, destino)
        ('\33[94m> Passagens que saem de \33[93m' +
         partida + ' e vão até ' + destino + '\33[94m')
        if len(self.lista) > 0:
            for elemento in self.lista:
                if elemento.get('Partida').lower() == partida.lower() and elemento.get('Destino').lower() == destino.lower():
                    palavras += '\n' + '-'*90
                    palavras += '\nVoo: ' + elemento.get('Voo') + ' Preço: R$' + str(
                        elemento['Preço']) + '\nLocal de partida: ' + elemento['Partida'] + ' |  Local de destino: ' + elemento['Destino']
                    palavras += '\nData de ida: ' + elemento['DataPartida'] + ' |  Horário da ida: ' + elemento['HoraPartida'] + \
                        '\nData de chegada: ' + \
                        elemento['DataChegada'] + \
                        ' | Horário da chegada: ' + elemento['HoraChegada']
        else:
            palavras += '\n' + '-'*90
            palavras += 'Não encontrei resultados para essa consulta :c'
        return palavras

    def mostrarVoo(self, voo):
        palavras = ''
        for elemento in self.lista:
            if elemento.get('Voo').lower() == voo.lower():
                palavras += '\nVoo: ' + elemento.get('Voo') + ' Preço: R$' + str(
                    elemento['Preço']) + '\nLocal de partida: ' + elemento['Partida'] + ' |  Local de destino: ' + elemento['Destino']
                palavras += '\nData de ida: ' + elemento['DataPartida'] + ' |  Horário da ida: ' + elemento['HoraPartida'] + \
                    '\nData de chegada: ' + \
                    elemento['DataChegada'] + \
                    ' | Horário da chegada: ' + elemento['HoraChegada']
        if palavras == '':
            palavras += 'Ops, ocorreu um erro'
        return palavras