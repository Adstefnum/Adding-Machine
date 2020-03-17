import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout



class Design(GridLayout):

    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"
    


class simplecalc(App):
    def build(self):
        return Design()

simplecalc().run()
