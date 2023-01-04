from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):

    def build(self):
        label = MDLabel(text='Olá mundo', halign='center', theme_text_color='Custom', text_color=(0, 1, 0, 1)) 
        return label


MainApp().run()