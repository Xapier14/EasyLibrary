import PySimpleGUI as sg
from controller.controllerInterface import ControllerInterface

class LoginController(ControllerInterface):
    def EventLoop(event, values, model):
        if (values != None):
            model.username = values["-username-"]
            model.password = values["-password-"]
        match (event):
            case sg.WIN_CLOSED:
                return True
        return
