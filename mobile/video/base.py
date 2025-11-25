from kivymd.app import MDApp
from kivy.lang import Builder

kv = '''
FloatLayout:
    MDRaisedButton:
        text: "Clica em mim!"  
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

MyApp().run()