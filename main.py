from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from code import math
from code import key
from code import idk
import random

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)


class MenuScreen(Screen):

    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        bl = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.75, .75), pos=(250, 100))
        bl.add_widget(Button(text="idk", on_press=lambda x: set_screen('idk'), size_hint=(0.7, .5), pos=(350, 200)))
        bl.add_widget(Button(text="Math", on_press=lambda x: set_screen('math'), size_hint=(0.7, .5), pos=(350, 200)))
        self.add_widget(bl)


class I_dont_know(Screen):

    def __init__(self, **kw):
        super(I_dont_know, self).__init__(**kw)

    def on_enter(self):
        al = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, .1))
        al.add_widget(Button(text="Back", on_press=lambda x: set_screen('menu'), size_hint=(.5, 1)))
        bl = BoxLayout(orientation='vertical', padding=15)
        self.gl = GridLayout(cols=2, spacing=15, size_hint=(1, .4))
        self.qst_on = Label(text='')
        bl.add_widget(al)
        bl.add_widget(self.qst_on)
        self.btn1 = Button(text='answ')
        self.btn2 = Button(text='answ')
        self.btn3 = Button(text='answ')
        self.btn4 = Button(text='answ')
        self.gl.add_widget(self.btn1)
        self.gl.add_widget(self.btn2)
        self.gl.add_widget(self.btn3)
        self.gl.add_widget(self.btn4)
        bl.add_widget(self.gl)
        self.add_widget(bl)
        self.generate_q()
        self.generate_answ()
        self.check_answ()

        # генерация начального вопроса

    def generate_q(self):
        rand_num_qst = random.randint(0, len(math))
        random_question = key(idk, rand_num_qst)
        self.qst_on.text = str(random_question)
        self.saved_qst = random_question

    def generate_answ(self):
        self.random_nums_anws = list(range(0, 4))
        random.shuffle(self.random_nums_anws)
        self.btn1.text = str(idk.get(self.saved_qst)[self.random_nums_anws[0]])
        self.btn2.text = str(idk.get(self.saved_qst)[self.random_nums_anws[1]])
        self.btn3.text = str(idk.get(self.saved_qst)[self.random_nums_anws[2]])
        self.btn4.text = str(idk.get(self.saved_qst)[self.random_nums_anws[3]])

        if len(idk.get(self.saved_qst)) > 3:
            pass
        # мне не очень хочется делать вставку картинки пока что

    def check_answ(self):
        for i in math:
            a = i
            if self.btn1 == a:
                self.btn1 = Button(text='answ', background_color=(1, 2, 7, 1))
            elif self.btn2 == a:
                self.btn2 = Button(text='answ', background_color=(1, 2, 7, 1))
            elif self.btn3 == a:
                self.btn3 = Button(text='answ', background_color=(1, 2, 7, 1))
            elif self.btn4 == a:
                self.btn4 = Button(text='answ', background_color=(1, 2, 7, 1))




class Math(Screen):

    def __init__(self, **kw):
        super(Math, self).__init__(**kw)

    def on_enter(self):
        al = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, .1))
        al.add_widget(Button(text="Back", on_press=lambda x: set_screen('menu'), size_hint=(.5, 1)))
        bl = BoxLayout(orientation='vertical', padding=15)
        self.gl = GridLayout(cols=2, spacing=15, size_hint=(1, .4))
        self.qst_on = Label(text='')
        bl.add_widget(al)
        bl.add_widget(self.qst_on)
        self.btn1 = Button(text='answ', on_press=self.check_answ)
        self.btn2 = Button(text='answ', on_press=self.check_answ)
        self.btn3 = Button(text='answ', on_press=self.check_answ)
        self.btn4 = Button(text='answ', on_press=self.check_answ)
        self.gl.add_widget(self.btn1)
        self.gl.add_widget(self.btn2)
        self.gl.add_widget(self.btn3)
        self.gl.add_widget(self.btn4)
        bl.add_widget(self.gl)
        self.add_widget(bl)
        self.generate_q()
        self.generate_answ()
        # генерация начального вопроса

    def generate_q(self):
        rand_num_qst = random.randint(0, len(math))
        random_question = key(math, rand_num_qst)
        self.qst_on.text = str(random_question)
        self.saved_qst = random_question

    def generate_answ(self):
        random_nums_anws = list(range(0, 4))
        random.shuffle(random_nums_anws)
        self.btn1.text = str(math.get(self.saved_qst)[random_nums_anws[0]])
        self.btn2.text = str(math.get(self.saved_qst)[random_nums_anws[1]])
        self.btn3.text = str(math.get(self.saved_qst)[random_nums_anws[2]])
        self.btn4.text = str(math.get(self.saved_qst)[random_nums_anws[3]])

        if len(math.get(self.saved_qst)) > 3:
            pass
        # мне не очень хочется делать вставку картинки пока что

    def check_answ(self, instance):
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
