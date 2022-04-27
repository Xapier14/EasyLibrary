import PySimpleGUI as sg
import app
import make
from controller.baseController import Controller

class LoginController(Controller):
    def EventLoop(self, event, values, model):
        if (values != None):
            model.username = values["-username-"]
            model.password = values["-password-"]
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case "OK":
                model.username = ""
                model.password = ""
                app.PushPairToStack(make.MakeSelfService())
                return True
        return False
