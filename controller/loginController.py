import PySimpleGUI as sg
import app
import make
from controller.controllerInterface import ControllerInterface

class LoginController(ControllerInterface):
    def EventLoop(self, event, values, model):
        if (values != None):
            model.username = values["-username-"]
            model.password = values["-password-"]
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case "OK":
                app.PushPairToStack(make.MakeSelfService())
                print("EVENT OK!")
                return True
        return False
