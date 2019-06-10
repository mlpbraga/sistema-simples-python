from datetime import datetime
from viagens import *

class Usuario:
    def __init__(self):
        self.dados = dict()

    def cadastrar(self):
        print('\33[94m> Preencha os seguintes dados de cadastro.')
        self.dados['Usuario'] = input('>> Usuario: ')
        self.dados['Senha'] = input('>> Senha: ')
        confirma = input('>> Confirme sua senha: ')
        while confirma != self.dados['Senha']:
            print('\33[95m> As senhas não corrependem.\33[94m')
            confirma = input('>> Confirme sua senha: ')
        self.dados['Nome'] = input('>> Nome: ')
        nasc = input('>> Ano de Nascimento: ')
        self.dados['Idade'] = datetime.now().year - int(nasc)
        self.dados['CPF'] = input('>> CPF(nt para estrangeiros): ')
        self.dados['Email'] = input('>> Email: ')
        self.dados['Telefone'] = input('>> Telefone: ')
        self.dados['Endereço'] = input('>> Endereço: ')
        if self.dados['CPF'] == 'nt':
            self.dados['passaporte'] = input('>> Número do passaporte: ')

        print('\33[94m-' * 35 + ' Confirme seus dados ' + '-' * 35 + '\33[93m-')
        for k, v in self.dados.items():
            print(f' - {k}: {v}')
        print('-'*90)
        correct = ''
        while correct not in ['N', 'n', 'nao', 'S', 's', 'sim']:
            correct = input("\33[94m> Seus dados estão corretos?(S/n): ")
            if correct in ['N', 'n', 'nao']:
                print('> Reinicie o cadastro, porfavor')
                self.__init__()
            elif correct in ['S', 's', 'sim']:
                print('\33[92m> Cadastro realizado com sucesso!\33[94m')
                with open('person.csv', 'a+') as f:
                    ultima = list(self.dados.keys())[-1]
                    for chave in self.dados.keys():
                        f.write(chave + ':' + str(self.dados[chave]))
                        if chave == ultima:
                            f.write(';\n')
                        else:
                            f.write(',')
                novo = open('viagens-' + self.dados['Usuario'].lower() + '.csv', 'w')
                novo.close()
                return 2
            else:
                print('\33[95m> Responda S para sim ou N para não.\33[94m')

    def entrar(self, user, senha):
        with open('person.csv', 'r') as f:
            dados = f.readlines()
            usuario = dict({})
            for dado in dados:
                usario_valido = 'Usuario:'+user in dado
                senha_valida = 'Senha:'+senha in dado
                if usario_valido and senha_valida:
                    atributos = dado.strip(';').split(',')
                    for atributo in atributos:
                        chave_valor = atributo.split(':')
                        usuario[chave_valor[0]] = chave_valor[1]
                    self.dados = usuario
                    print('\33[92m> Bem vindo(a), ' + self.dados['Nome'] + '.\33[94m') 

                    return self.dados
        
        print('\33[95m> Usuário ou senha não encontrados.\33[94m') 
        return None

    def inserirViagem(self, viagem):
        with open('viagens-' + self.dados['Usuario'].lower() + '.csv', 'a+') as f:
            ultima = list(viagem.keys())[-1]
            for chave in viagem.keys():
                f.write(chave + ':' + str(viagem[chave]))
                if chave == ultima:
                    f.write(';')
                else:
                    f.write(',')
        print('\33[92m> Você inseriu uma viagem na sua lista! a cobrança das')
        print('passagens será enviada para o seu e-mail em até 5 dias.\33[94m')
    
    def removerViagem(self, voo):
        with open('viagens-' + self.dados['Usuario'].lower() + '.csv', 'a+') as f:
            dados = f.readlines()
            aux = ''
            for dado in dados:
                if 'Voo:'+voo not in dado:
                    aux = aux + dado
        
        with open('viagens-' + self.dados['Usuario'].lower() + '.csv', 'w') as f:
            f.write(aux)

        print('\33[92m> Você removeu essa uma viagem na sua lista!')
        print('A cobrança das passagens será cancelada.\33[94m')

    def imprimirViagens(self, menuCompras=False):
        v = Viagens('viagens-' + self.dados['Usuario'].lower() + '.csv')
        v.listarTodas(menuCompras=False)