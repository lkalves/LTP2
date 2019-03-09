from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Test(App):
	def build(self):
		box = BoxLayout(orientation='vertical')

		button = Button(text='Botão!', on_release=self.incrementar)
		self.label = Label(text='1')

		box.add_widget(button)
		box.add_widget(self.label)

		return box

	def incrementar(self, button):
		self.label.text = str(int(self.label.text)+1)

	def bola(self):
		pass
		
Test().run()

