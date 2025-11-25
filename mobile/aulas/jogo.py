from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class TicTacToe(GridLayout):
    def __init__(self, **kwargs):
        super(TicTacToe, self).__init__(**kwargs)
        self.cols = 3
        for i in range(9):
            btn = Button(text='', font_size=32)
            btn.bind(on_press=self.player_move)
            self.add_widget(btn)

    def player_move(self, button):
        if button.text == '':
            button.text = 'X'

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()
    
if __name__ == "__main__":
    TicTacToeApp().run()