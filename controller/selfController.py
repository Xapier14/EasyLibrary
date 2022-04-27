# Controller for Self-Service mode
import PySimpleGUI as sg
import app
from controller.controllerInterface import ControllerInterface

class SelfController(ControllerInterface):
    def EventLoop(self, event, values, model):
        if (values != None):
            model.username = values["-username-"]
            model.password = values["-password-"]
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
        return False