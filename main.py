import math
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

from kivy.core.window import Window

Window.size=(450,800)

JANELA_1 = """
ScreenManager:
    Main:
        name: 'main'
<Main>:
    MDFloatLayout:
        id: _TELA_
        md_bg_color: 0.941,0.941,0.941,1
        FitImage:
            source: 'background_black.png'
            pos_hint: {'center_y': 0.95, 'center_x': 0.5}
            size_hint: 1,0.12
        MDLabel:
            text: 'CONSTRUTOR' # constructor
            color: 'white'
            halign: 'center'
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '40'
            pos_hint: {'center_y': 0.94, 'center_x': 0.5}
        MDLabel:
            markup: True
            text: 'Largura do Piso[font=Fonts/aller.bold-italic.ttf][size=24] / [/size][/font]Parede:' # floor/wall width
            halign: 'center'
            pos_hint: {'center_y': 0.855, 'center_x': 0.5}
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '34'
        MDTextFieldRect:
            id: _LARGPISO_
            hint_text: '0,00'
            height: "35dp"
            normal_color: app.theme_cls.accent_color
            background_color: '#4b4947'
            foreground_color: '#ffffff'
            pos_hint: {'center_y': 0.805, 'center_x': 0.35}
            size_hint: 0.19, 0.045
            font_name: 'Fonts/aller.bold-italic.ttf'
            font_size: '22'
        MDLabel:
            text: '(metros)'
            color: '#4b4947'
            halign: 'center'
            pos_hint: {'center_y': 0.805, 'center_x': 0.58}
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '28'
        MDSeparator:
            height: '2dp'
            pos_hint: {'center_y': 0.765, 'center_x': 0.5}
            color: '#adaaa8'
            size_hint_x: '0.1'
        MDLabel:
            markup: True
            text: 'Comprimento do Piso[font=Fonts/aller.bold-italic.ttf][size=24] / [/size][/font]' # Floor Length
            halign: 'center'
            pos_hint: {'center_y': 0.735, 'center_x': 0.5}
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '34'
        MDLabel:
            text: 'Altura da Parede:'
            halign: 'center'
            pos_hint: {'center_y': 0.695, 'center_x': 0.5}
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '34'
        MDTextFieldRect:
            id: _COMPRPISO_
            hint_text: '0,00'
            height: "35dp"
            normal_color: app.theme_cls.accent_color
            background_color: '#4b4947'
            foreground_color: '#ffffff'
            pos_hint: {'center_y': 0.64, 'center_x': 0.35}
            size_hint: 0.19, 0.045
            font_name: 'Fonts/aller.bold-italic.ttf'
            font_size: '22'
        MDLabel:
            text: '(metros)'
            color: '#4b4947'
            halign: 'center'
            pos_hint: {'center_y': 0.64, 'center_x': 0.58}
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '28'
        MDSeparator:
            height: '2dp'
            pos_hint: {'center_y': 0.60, 'center_x': 0.5}
            color: '#adaaa8'
            size_hint_x: '0.1'
        MDLabel:
            text: 'Largura da Peça:'
            halign: 'center'
            pos_hint: {'center_y': 0.57, 'center_x': 0.5}
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '34'
        MDTextFieldRect:
            id: _LARGPECA_
            hint_text: '0,00'
            height: "35dp"
            normal_color: app.theme_cls.accent_color
            background_color: '#4b4947'
            foreground_color: '#ffffff'
            pos_hint: {'center_y': 0.515, 'center_x': 0.35}
            size_hint: 0.19, 0.045
            font_name: 'Fonts/aller.bold-italic.ttf'
            font_size: '22'
        MDLabel:
            text: '(centímetros)'
            color: '#4b4947'
            halign: 'center'
            pos_hint: {'center_y': 0.515, 'center_x': 0.63}
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '25'
        MDSeparator:
            height: '2dp'
            pos_hint: {'center_y': 0.475, 'center_x': 0.5}
            color: '#adaaa8'
            size_hint_x: '0.1'
        MDLabel:
            text: 'Comprimento da Peça:'
            halign: 'center'
            pos_hint: {'center_y': 0.445, 'center_x': 0.5}
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '34'
        MDTextFieldRect:
            id: _COMPRPECA_
            hint_text: '0,00'
            height: "35dp"
            normal_color: app.theme_cls.accent_color
            background_color: '#4b4947'
            foreground_color: '#ffffff'
            pos_hint: {'center_y': 0.39, 'center_x': 0.35}
            size_hint: 0.19, 0.045
            font_name: 'Fonts/aller.bold-italic.ttf'
            font_size: '22'
        MDLabel:
            text: '(centímetros)'
            color: '#4b4947'
            halign: 'center'
            pos_hint: {'center_y': 0.39, 'center_x': 0.63}
            font_name: 'Fonts/challenge.contour.ttf'
            font_size: '25'
        MDSeparator:
            height: '2dp'
            pos_hint: {'center_y': 0.335, 'center_x': 0.5}
            color: '#adaaa8'
            #size_hint_x: '0.85'
        MDRaisedButton:
            id: 'calc'
            markup: True
            text: '[font=Fonts/aller.bold-italic.ttf]CALCULAR[/font]'
            font_size: '25sp'
            pos_hint: {'center_y': 0.285, 'center_x': 0.5}
            md_bg_color: 0.173,0.157,0.145,1
            on_release:
                root.calcular()
        
        MDSeparator:
            height: '2dp'
            pos_hint: {'center_y': 0.23, 'center_x': 0.5}
            color: '#adaaa8'
"""

class Main(Screen):
    def calcular(self):

        largura_piso = self.ids._LARGPISO_.text.replace(',', '.')
        largura_piso = float(largura_piso)

        comprimento_piso = self.ids._COMPRPISO_.text.replace(',', '.')
        comprimento_piso = float(comprimento_piso)

        largura_peca = self.ids._LARGPECA_.text.replace(',', '.')
        largura_peca = float(largura_peca)

        comprimento_peca = self.ids._COMPRPECA_.text.replace(',', '.')
        comprimento_peca = float(comprimento_peca)

        areatotal = largura_piso * comprimento_piso
        tamanhopeca = (largura_peca/100) * (comprimento_peca/100)
        quantidade = areatotal / tamanhopeca
        quantidade = math.ceil(quantidade)

        texto = MDLabel(markup=True, text = '[font=Fonts/challenge.contour.ttf][color=#2c2825][size=30]Para a área informada,\nserão necessárias[/font][/color][/size]',pos_hint = {'center_x': 0.5, 'center_y': 0.165},halign = 'center')
        self.ids._TELA_.add_widget(texto)

        self.quantidadepecasview = MDLabel(markup=True, text = f'[font=Fonts/challenge.contour.ttf][color=#2c2825][size=50]{quantidade:.0f} Peças[/font][/color][/size]',pos_hint = {'center_x': 0.5, 'center_y': 0.08}, halign = 'center')
        self.ids._TELA_.add_widget(self.quantidadepecasview)

class Calc(MDApp):
    def build(self):
        return Builder.load_string(JANELA_1)

Calc().run()
