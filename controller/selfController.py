# Controller for Self-Service mode
import PySimpleGUI as sg
import app
from controller.baseController import Controller

class SelfController(Controller):
    def EventLoop(self, event, values, model):
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
        return False
    
    def Update(self, model):
        return