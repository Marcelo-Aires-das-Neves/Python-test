from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class Ola(Label):
    pass
    
class Testkiv(App):
    def build(self):
        return  Ola()

Testkiv().run()