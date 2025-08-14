from kivy.app import App
from kivy.uix.label import Label

class RecipePlannerApp(App):
    def build(self):
        return Label(text="Hello, Recipe Planner!")

if __name__ == "__main__":
    RecipePlannerApp().run()