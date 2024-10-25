from kivy.app import App
from kivy.lang import Builder

class TestApp(App):
    def build(self):
        return  Builder.load_file('testkiv.kv')

TestApp().run()