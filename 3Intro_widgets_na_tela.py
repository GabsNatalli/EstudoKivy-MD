from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder

# class MainApp(MDApp):

#     def build(self):
        
#         fl = MDFloatLayout()

#         btn = MDRaisedButton(
#             text='OK',
#             pos_hint={'center_x': 0.5, 'center_y': 0.5}
#         )

#         fl.add_widget(btn)

#         return fl

# MainApp().run()

##################################################################################################################################
# O que está abaixo faz o que está a cima na linguagem KIVY / isso serve para separarmos nossa interface do nosso codigo principal.
##################################################################################################################################


# KV = """
# MDScreen:

#     MDRaisedButton:
#         text: "Ok"
#         pos_hint: {"center_x": 0.5, "center_y": 0.5}
# """

# class MainApp(MDApp):
    
#     def build(self):        
#         return Builder.load_string(KV)

#     def funcao(self):
#         pass

# MainApp().run()

#####################################################

class TesteApp(MDApp):
    
    def build(self):        
        pass

TesteApp().run()  # continua no 4 arquivo