from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout  # Importe o BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget



print("1")
Main_GUI=Builder.load_file("main_frame_design.kv")

class Main_window(App):
    def build(self):
        self.title="analise de portifolio"
        return Main_GUI

    def on_start(self):

        pass

    def portifolio_scroll_update(self, portfolio_namelist):
        new_layout = BoxLayout(orientation='vertical', spacing=20, size_hint_y=None)

        for stock in portfolio_namelist:
            label = Label(text=stock)
            new_layout.add_widget(label)

        new_scrollview = ScrollView(pos_hint={'x': -0.25, 'y': -0.25})
        new_scrollview.add_widget(new_layout)

        # Verifica se já existe um ScrollView chamado "stocks_scroll" no root
        if "stocks_scroll" in self.root.ids:
            # Limpa todos os widgets dentro do ScrollView existente
            self.root.ids["stocks_scroll"].clear_widgets()
            # Adiciona o novo ScrollView ao layout principal
            self.root.ids["stocks_scroll"].add_widget(new_scrollview)




Main_window().run()
print("ok")