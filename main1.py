from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


with open('borel.kv', encoding='utf8') as f:
    Builder.load_string(f.read())

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tarefas(Screen):
    def __init__(self, tarefas=[],**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas: #tarefas =['andre','ugb']
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text=''

class Sobre(Screen):
    def addWidget2(self):
        label2 = Label(text='O Kivy é Brabo!')
        self.ids.box2.add_widget(Label(text="dsgdgsdgsdfsdfsdf"))

class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text=text

class Borelzada(App):
    def build(self):
        self.icon='kivy.jpg'
        return Gerenciador()


Borel().run()
Borelzada().run()
