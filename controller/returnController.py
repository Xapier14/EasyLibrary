# Controller for 
import PySimpleGUI as sg
import app
import data
from controller.baseController import Controller

class ReturnController(Controller):
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
        datastore = data.GetDataStore()
        model.transactions = datastore.GetTransactions(model.user.GetUsername(), True)
        model.globalBooks = datastore.GetAllBooks()
        model.localBooks = []
        for transaction in model.transactions:
            model.localBooks.append(datastore.GetBookItem(transaction.GetItemCode()))
        self.ModelUpdated(model)
        return

    def WinClose(self):
        app.PopControllerFromStack();
        return True
    
    def Update(self, model):
        return