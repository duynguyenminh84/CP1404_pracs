from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Layout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Cristiano Ronaldo", "Lionel Messi", "Neymar Junior", "Eden Hazard"]
        self.add_labels()

    def add_labels(self):
        for name in self.names:
            label = Label(text=name)
            self.add_widget(label)


class DynamicLabelsApp(App):
    def build(self):
        return Layout()


DynamicLabelsApp().run()