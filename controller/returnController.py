# Controller for 
import PySimpleGUI as sg
import app
import data
import imageTool
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
            case "-button-back-":
                if (self.button_back(model)):
                    return True
            case "-button-return-":
                if (self.button_return(model, values["-transaction-id-"])):
                    return True
        # check if event is table event
        if type(event) is tuple:
            if event[0] == "-table-" and event[2][0] != None:
                if (event[2][0] >= 0):
                    if (self.table_update(event[2][0], model)):
                        return True
        return False

    def Init(self, model):
        datastore = data.GetDataStore()
        model.transactions = datastore.GetTransactions(model.user.GetUsername(), True)
        model.globalBooks = datastore.GetAllBooks()
        for transaction in model.transactions:
            model.localBooks.append(datastore.GetBookItem(transaction.GetItemCode()))
        model.coverImage = imageTool.MakeSizedImage(datastore.GetImage(), (320, 320))
        self.ModelUpdated(model)
        return

    def WinClose(self):
        return False
    
    def Update(self, model):
        return

    def button_back(self, model):
        app.PopControllerFromStack()
        return True

    def button_return(self, model, transactionId):
        datastore = data.GetDataStore()
        transaction = datastore.GetTransaction(transactionId)
        return False
    
    def table_update(self, row, model):
        if row >= 0:
            transaction = model.transactions[row]
            model.selectedTransaction = transaction

            localBook = None

            for local in model.localBooks:
                if transaction.GetItemCode() == local.GetItemCode():
                    localBook = local
                    break
            
            datastore = data.GetDataStore()
            model.coverImage = imageTool.MakeSizedImage(datastore.GetImage(localBook.GetISBN()), (320, 320))
            self.ModelUpdated(model)
        else:
            model.selectedTransaction = None
            model.coverImage = None
            self.ModelUpdated(model)
        return False