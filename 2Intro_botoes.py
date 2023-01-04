from kivymd.app import MDApp

from kivy.core.window import Window    # Importação do KIVY e não do KIVY MD. -> USAMOS TAL IMPORTAÇÃO PARA MODELAGEM DA NOSSA INTERFACE.
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton, MDFloatingActionButton, MDRectangleFlatButton, MDRaisedButton, MDRectangleFlatIconButton # Criação de botão de texto 
# / botão de icon / botão flutuante / botão retangular / botão retangular flutuante / botão retangular com texto e icone

class MainApp(MDApp):

    Window.size = (400, 600)        # usamos Size para definirmos o tamanho da nossa tela 


    def build(self):

        boxLayout = MDBoxLayout(
            orientation='vertical',
            spacing=15,                                 # Propriedade para espaçamento dos conteudos da BOX
            pos_hint={'center_x': 0.5, 'center_y': 0.8}   # Centralizando os conteudos da nossa BOX
        )                           # Criação da BOX


        bttn1 = MDFlatButton(
            text='Login',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}  # Centralizando o Botão.
        )                           # Botão para a BOX

        bttn2 = MDIconButton(
            icon='home',  # Aqui vai buscar um icone que o proprio KIVY tem, através do código do mesmo.
            pos_hint={'center_x': 0.5, 'center_y': 0.5} 
        )                         
        
        bttn3 = MDFloatingActionButton(
            icon='plus',  # Aqui vai buscar um icone que o proprio KIVY tem, através do código do mesmo.
            pos_hint={'center_x': 0.5, 'center_y': 0.5} 
        ) 

        bttn4 = MDRectangleFlatButton(
            text='TESTE',  # Aqui vai buscar um icone que o proprio KIVY tem, através do código do mesmo.
            pos_hint={'center_x': 0.5, 'center_y': 0.5} 
        ) 

        bttn5 = MDRaisedButton(
            text='TESTE2',  # Aqui vai buscar um icone que o proprio KIVY tem, através do código do mesmo.
            pos_hint={'center_x': 0.5, 'center_y': 0.5} 
        ) 

        bttn6 = MDRectangleFlatIconButton(
            icon='folder',
            text='TESTE3',  # Aqui vai buscar um icone que o proprio KIVY tem, através do código do mesmo.
            pos_hint={'center_x': 0.5, 'center_y': 0.5} 
        ) 

        boxLayout.add_widget(bttn1)  # Adicionando botão de texto.
        boxLayout.add_widget(bttn2)  # Adicionando botão de icone.
        boxLayout.add_widget(bttn3)  # Adicionando botão flutuante.
        boxLayout.add_widget(bttn4)  # Adicionando botão retangular.
        boxLayout.add_widget(bttn5)  # Adicionando botão retangular flutuante.
        boxLayout.add_widget(bttn6)  # Adicionando botão retangular com texto e icone.


        return boxLayout


MainApp().run()