from kivymd.app import MDApp
from kivy.lang import Builder

kv = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Minha App"
        FormLogin:

<FormLogin@FloatLayout>:
    MDIconButton:
        icon: 'account' 
        icon_size: "75sp"
        pos_hint: {"center_x": .5, "center_y": .8}

    MDTextField:
        size_hint_x: .7
        hint_text: 'Email'
        pos_hint: {"center_x": .5, "center_y": .6}

    MDTextField:
        size_hint_x: .7
        hint_text: 'Senha'
        pos_hint: {"center_x": .5, "center_y": .5}

    MDFillRoundFlatButton:
        text: 'Login'
        pos_hint: {"center_x": .5, "center_y": .4}

    MDLabel:
        text: 'Esqueceu sua senha?'
        halign: 'center'
        pos_hint: {"center_y": .3}

    MDTextButton:
        text: 'Clique aqui!'
        pos_hint: {"center_x": .5, "center_y": .2}
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

MyApp().run()
