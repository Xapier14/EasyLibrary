import PySimpleGUI as sg
from view.viewInterface import ViewInterface

class LoginView(ViewInterface):
    def ConstructLayout(self, model):
        layout = [  [sg.Text("Hello ROW 1")],
                    [sg.Text("Hello ROW 2")],
                    [sg.Input(key="-username-" , default_text=model.username)],
                    [sg.Input(key="-password-", default_text=model.password, password_char="*")],
                    [sg.Button("OK")] ]
        return layout