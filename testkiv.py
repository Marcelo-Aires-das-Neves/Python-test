from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (600, 500)
Window.clearcolor = (233/255, 225/255, 216/255, 1)

class Cadastro(BoxLayout):
    pass
    
class Testkiv(App):
    def build(self):
        return  Cadastro()

Testkiv().run()