import kivy
kivy.require('1.11.1')  # replace with your current Kivy version

from kivy.app import App
from kivy.uix.label import Label

class HelloWorld(App):
    def build(self):
        return Label(text='Hello, world!')

if __name__ == '__main__':
    HelloWorld().run()
