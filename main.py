from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)


class MenuScreen(Screen):

    def build(self):
        bl = BoxLayout(orientation='vertical', padding=15)
        bl.add_widget(Button(text="PART1"))
        bl.add_widget(Button(text="PART2"))
        bl.add_widget(Button(text="PART3"))
        bl.add_widget(Button(text="PART4"))
        return bl

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

class MyApp(App):

    def build(self):
        bl = BoxLayout(orientation='vertical', padding=15)
        gl = GridLayout(cols=2, spacing=15, size_hint=(1, .4))
        lbl = Label(text='some_text')
        bl.add_widget(lbl)

        gl.add_widget(Button(text="ANS_0"))
        gl.add_widget(Button(text="ANS_1"))
        gl.add_widget(Button(text="ANS_2"))
        gl.add_widget(Button(text="ANS_3"))
        bl.add_widget(gl)
        return bl

if __name__ == '__main__':
    MyApp().run()
