from kivy.app import App
from kivy.uix.label import Label

class Ola(Label):
    pass
    
class Testkiv(App):
    def build(self):
        return  Ola()

Testkiv().run()