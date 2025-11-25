from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp

class MyApp(App):
    def build(self):
        # Objeto cont
        self.cont = 0
        # Objeto label 
        self.label = Label(
            text=str(self.cont), # Transforma cont em str 
            font_size=dp(40), # dp é densidade de pixels
            size_hint_y=0.2, 
            color=(1,1,1,1),              
        )
        
        layout = BoxLayout(orientation='vertical') # Orientação do layout 

        bnt1 = Button( 
            text="+",
            background_normal='', # Removendo cor normal
            background_color=(0, 1, 0, 1), # Adicionando nova cor          
            size_hint_y=0.4

        )
        
        bnt2 = Button(
            text='-',
            background_normal='',
            background_color=(1, 0, 0, 1),
            size_hint_y=0.4
        )

        bnt1.bind(on_press=self.soma) # Ligando com bind a função 
        bnt2.bind(on_press=self.sub)

        layout.add_widget(bnt1) # Adicionando widgets na tela
        layout.add_widget(self.label)
        layout.add_widget(bnt2)

        return layout

    def soma(self, instance):
        self.cont += 1
        self.label.text = str(self.cont) # Atualiza o texto do botão para o valor do cont

    def sub(self, instance):
        self.cont -= 1
        self.label.text = str(self.cont)

if __name__ == "__main__":
     MyApp().run()
