from kivy.app import App
from kivy.uix.widget import Widget

class TestWidget(Widget):
    pass

class RecipePlannerApp(App):
    def build(self):
        return TestWidget()

if __name__ == "__main__":
    RecipePlannerApp().run()