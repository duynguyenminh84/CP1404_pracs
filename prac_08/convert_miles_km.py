
"""
CP1404/CP5632 Practical - Suggested Solution
GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
Print statements included to see when the functions run
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class Converter(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        self.title = "Converting miles to kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate(self, text):
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def increment(self, text, change):
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * 1.60934)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


Converter().run()
