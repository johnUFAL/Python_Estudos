from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# =========================
# HERANÇA -> MeuBotao herda de Button
# =========================
class MeuBotao(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # chama o construtor da classe mãe (Button)
        self.__estado = "Inicial"   # ENCAPSULAMENTO (atributo privado com __)
        self.text = "Clique-me!"
        self.bind(on_press=self.on_button_click)

    # =========================
    # ENCAPSULAMENTO -> Getter e Setter
    # =========================
    def get_estado(self):
        return self.__estado

    def set_estado(self, novo_estado):
        self.__estado = novo_estado

    # =========================
    # POLIMORFISMO -> sobrescrevendo método herdado
    # (sobrescreve on_press para comportamento personalizado)
    # =========================
    def on_button_click(self, instance):
        self.text = "Clicou!"
        self.set_estado("Clicado")  # altera estado interno


# Outra classe herdando e polimorfando de novo
class MeuBotaoVerde(MeuBotao):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 1, 0, 1)  # verde
        self.text = "Botão Verde!"

    # Sobrescreve o comportamento do clique
    def on_button_click(self, instance):
        self.text = "Verde Clicado!"
        self.set_estado("Clicado Verde")


# Aplicativo principal
class MeuApp(App):
    def build(self):
        layout = BoxLayout()
        
        # Usando herança
        botao1 = MeuBotao()
        
        # Usando polimorfismo (mesma base, mas comportamento diferente)
        botao2 = MeuBotaoVerde()
        
        layout.add_widget(botao1)
        layout.add_widget(botao2)

        return layout


if __name__ == "__main__":
    MeuApp().run()
