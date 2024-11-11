from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (600, 500)
Window.clearcolor = (233/255, 225/255, 216/255, 1)

usuarios = {}

class Cadastro(BoxLayout):
    def cadastrar(self):
        nome = self.ids.nome.text
        saldo = self.ids.saldo.text
        if nome in usuarios:
            self.ids.msg.text = "Usuário já cadastrado"
        else:
            usuarios[nome] = float(saldo)
            self.ids.msg.text = "Usuário cadastrado com sucesso"
            self.ids.nome.text = ""
            self.ids.saldo.text = ""
            print(usuarios)
        
class Testkiv(App):
    def build(self):
        return  Cadastro()

Testkiv().run()