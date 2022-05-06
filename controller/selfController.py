# Controller for Self-Service mode
import PySimpleGUI as sg
import app
import make
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
            case "-button-search-":
                if (self.button_search(model)):
                    return True
            case "-button-borrow-":
                if (self.button_borrow(model)):
                    return True
            case "-button-return-":
                if (self.button_return(model)):
                    return True
            case "-button-due-":
                if (self.button_due(model)):
                    return True
            case "-button-history-":
                if (self.button_history(model)):
                    return True
            case "-button-logout-":
                if (self.button_logout(model)):
                    return True
        return False

    def WinClose(self):
        return False
    
    def Update(self, model):
        return

    def button_search(self, model):
        app.PushPairToStack(make.MakeSearchService())
        return True

    def button_borrow(self, model):
        app.PushPairToStack(make.MakeBorrowService(model.user))
        return True

    def button_return(self, model):
        app.PushPairToStack(make.MakeReturnService(model.user))
        return True

    def button_due(self, model):
        
        return True

    def button_history(self, model):
        
        return True

    def button_logout(self, model):
        app.PopControllerFromStack()
        return True