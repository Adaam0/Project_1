import kivy
import kivymd
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        hello_world = MDLabel(text = "Hello World")

        return hello_world
    

if __name__=='__main__':
    MyApp().run()