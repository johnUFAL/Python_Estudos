from kivymd.app import MDApp
from kivy.lang import Builder

#size_hint manipula o tamanho dos widgets 1,1 => a tela toda
#center tamanho do botao
#pos_hint para centralização

kv = '''
FloatLayout:
    MDRaisedButton:
        text: 'Botão 1'
        pos_hint: {'center_x': .5, 'center_y': .5}
    MDRaisedButton:
        text: 'Botão 2'
        size_hint_y: .12
        size_hint_x: 1
        pos_hint: {'center_y': .3}
    MDRaisedButton:
        text: 'Botão 3'
        pos_hint: {'center_x': .5, 'center_y': 0}
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

MyApp().run()