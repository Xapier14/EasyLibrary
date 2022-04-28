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
            case sg.WIN_X_EVENT:
                if (self.WinClose()):
                    return True
            case "-button-logout-":
                if (self.button_logout(model)):
                    return True
        return False

    def WinClose(self):
        return False
    
    def Update(self, model):
        return

    def button_logout(self, model):
        app.PopControllerFromStack()
        return True