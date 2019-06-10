from uteis import *


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
