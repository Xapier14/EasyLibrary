# Controller for Account Creation
import PySimpleGUI as sg
import app
from controller.baseController import Controller

class AccountController(Controller):
    def EventLoop(self, event, values, model):
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case sg.WIN_X_EVENT:
                if (self.WinClose()):
                    return True
        return False

    def Init(self, model):
        return

    def WinClose(self):
        app.PopControllerFromStack()
        return True
    
    def Update(self, model):
        return