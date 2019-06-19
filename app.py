from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button

from kivy.uix.label import Label

from kivy.uix.popup import Popup
import os

from usuarios import *
from viagens import *
from uteis import *

class Minhas(Screen):
    def mensagem(self, mensagem):
        self.ids['texto'].text = mensagem
        
    def voltar(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('connected')

    def remover(self, voo):
        app = App.get_running_app()
        app.objUsuario.removerViagem(voo)
        app.palavra = app.objUsuario.mostrarTodasViagens()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'minhas'
        self.manager.get_screen('minhas').mensagem(app.palavra)
        app.config.read(app.get_application_config())
        app.config.write()

class Compra(Screen):
    def mensagem(self, msg):
        self.ids['voo'].text = msg

    def ok(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'
        self.manager.get_screen('connected')

class Valormin(Screen):
    def show(self, valormini):
        app = App.get_running_app()
        app.palavra = via.mostrarPrecoMenor(valormini)
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'listagem'
        self.manager.get_screen('listagem').mensagem(app.palavra)

        app.config.read(app.get_application_config())
        app.config.write()

    def voltar(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('connected')

class Destino(Screen):
    def show(self, partida, destino):
        app = App.get_running_app()
        app.palavra = via.mostrarPartidaDestino(partida, destino)
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'listagem'
        self.manager.get_screen('listagem').mensagem(app.palavra)

        app.config.read(app.get_application_config())
        app.config.write()

    def voltar(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('connected')

class Connected(Screen):
    def listarTodas(self):
        app = App.get_running_app()
        app.palavra = via.mostrarTodas()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'listagem'
        self.manager.get_screen('listagem').mensagem(app.palavra)

        app.config.read(app.get_application_config())
        app.config.write()

    def listarPreco(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'valormin'
        self.manager.get_screen('valormin')

    def listarDestino(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'destino'
        self.manager.get_screen('destino')

    def listarMinhas(self):
        app = App.get_running_app()
        app.palavra = app.objUsuario.mostrarTodasViagens()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'minhas'
        self.manager.get_screen('minhas').mensagem(app.palavra)

        app.config.read(app.get_application_config())
        app.config.write()

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

class Listagem(Screen):
    def mensagem(self, mensagem):
        self.ids['texto'].text = mensagem

    def voltar(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('connected')

    def compra(self, voo):
        app = App.get_running_app()
        app.palavra = via.mostrarVoo(voo)
        pega = via.getVoo(voo)
        app.objUsuario.inserirViagem(pega)
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'compra'
        self.manager.get_screen('compra').mensagem(app.palavra)
        app.config.read(app.get_application_config())
        app.config.write()

class Signup(Screen):
    def do_signup(self, loginText, passwordText, nameText, dateText, adressText, cpfText, phoneText, mailText):
        app = App.get_running_app()
        app.username = loginText
        app.password = passwordText
        app.nome = nameText
        app.date = dateText
        app.adress = adressText
        app.cpf = cpfText
        app.phone = phoneText
        app.mail = mailText

        self.usr = Usuario()
        app.objUsuario = self.usr
        self.usr.cadastro(app.username, app.password, app.nome,
                          app.date, app.adress, app.cpf, app.phone, app.mail)
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'login'

        # self.manager.current = 'signup'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        chaves = self.ids.keys()
        for chave in chaves:
            self.ids[chave].text = ''

    def voltar(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText
        self.usr = Usuario()
        if self.usr.entrar(app.username, app.password):
            app.objUsuario = self.usr
            self.manager.transition = SlideTransition(direction='left')
            self.manager.current = 'connected'
        else:
            self.manager.current = 'login'
        app.config.read(app.get_application_config())
        app.config.write()

    def call_signup(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'signup'
        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ''
        self.ids['password'].text = ''


class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Signup(name='signup'))
        manager.add_widget(Listagem(name='listagem'))
        manager.add_widget(Valormin(name='valormin'))
        manager.add_widget(Destino(name='destino'))
        manager.add_widget(Compra(name='compra'))
        manager.add_widget(Minhas(name='minhas'))
        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )


if __name__ == '__main__':
    escreveArquivoViagens()
    via = Viagens()
    LoginApp().run()
