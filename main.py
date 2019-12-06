from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)


class MenuScreen(Screen):

    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        bl = BoxLayout(orientation='vertical', padding=15)
        bl.add_widget(Button(text="idk", on_press=lambda x: set_screen('idk')))
        bl.add_widget(Button(text="Math", on_press=lambda x: set_screen('math')))
        self.add_widget(bl)


class I_dont_know(Screen):

    def __init__(self, **kw):
        super(I_dont_know, self).__init__(**kw)

    def on_enter(self):
        al = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, .1))
        al.add_widget(Button(text="Back", on_press=lambda x: set_screen('menu'), size_hint=(.5, 1)))
        bl = BoxLayout(orientation='vertical', padding=15)
        gl = GridLayout(cols=2, spacing=15, size_hint=(1, .4))
        lbl = Label(text='some_text')
        bl.add_widget(al)
        bl.add_widget(lbl)

        gl.add_widget(Button(text="ANS_0"))
        gl.add_widget(Button(text="ANS_1"))
        gl.add_widget(Button(text="ANS_2"))
        gl.add_widget(Button(text="ANS_3"))
        bl.add_widget(gl)
        self.add_widget(bl)

    def generate_q(self):
        pass

    def generate_answ(self):
        pass


class Math(Screen):

    def __init__(self, **kw):
        super(Math, self).__init__(**kw)

    def on_enter(self):
        al = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, .1))
        al.add_widget(Button(text="Back", on_press=lambda x: set_screen('menu'), size_hint=(.5, 1)))
        bl = BoxLayout(orientation='vertical', padding=15)
        gl = GridLayout(cols=2, spacing=15, size_hint=(1, .4))
        lbl = Label(text='some_text')
        bl.add_widget(al)
        bl.add_widget(lbl)

        gl.add_widget(Button(text="ANS_0"))
        gl.add_widget(Button(text="ANS_1"))
        gl.add_widget(Button(text="ANS_2"))
        gl.add_widget(Button(text="ANS_3"))

        bl.add_widget(gl)
        self.add_widget(bl)

    def generate_q(self):
        pass

    def generate_answ(self):
        pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Math(name='math'))
sm.add_widget(I_dont_know(name='idk'))


def set_screen(name_screen):
    assert isinstance(name_screen, object)
    sm.current = name_screen


class TestApp(App):

    def build(self):
        set_screen('menu')
        return sm


if __name__ == '__main__':
    TestApp().run()
