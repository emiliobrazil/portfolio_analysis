from kivy.app import App
from kivy.lang import Builder
print("1")
Main_GUI=Builder.load_file("main_frame_design.kv")

class Main_window(App):
    def build(self):
        self.title="analise de portifolio"
        return Main_GUI
    
Main_window().run()
print("ok")