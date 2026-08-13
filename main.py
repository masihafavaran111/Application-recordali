from kivy.app import App
from kivy.uix.label import Label


class FavaranRecord(App):
    def build(self):
        return Label(text="فوران رکورد")


if __name__ == "__main__":
    FavaranRecord().run()
