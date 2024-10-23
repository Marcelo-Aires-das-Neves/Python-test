
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class HelloApp(App):
    def build(self):
        return Label(text='Hello World, Marcelo')
    
    
HelloApp().run()