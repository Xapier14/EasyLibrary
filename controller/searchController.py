# Controller for Self-Service search function
import PySimpleGUI as sg
import app
from controller.baseController import Controller

class SearchController(Controller):
    def EventLoop(self, event, values, model):
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case sg.WIN_X_EVENT:
                if (self.WinClose()):
                    return True
            case "-button-back-":
                if (self.button_back(model)):
                    return True
        return False

    def WinClose(self):
        return False
    
    def Update(self, model):
        return

    def button_back(self, model):
        app.PopControllerFromStack()
        return True