from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Ola(BoxLayout):
    def __init__(self):
        super().__init__()
        #self.orientation = 'horizontal'
        #self.add_widget('ola')
        #self.ids.textOla.text = 'ola'
        #self.ids['textPython'].text = 'Hello Python while Kivy'
        #print(self.ids)
        pass
    
class Testkiv(App):
    def build(self):
        return  Ola()

Testkiv().run()