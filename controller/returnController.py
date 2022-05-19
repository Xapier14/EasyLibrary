# Controller for 
import PySimpleGUI as sg
import app
import data
import imageTool
import dateTool
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
        transaction = datastore.GetTransaction(int(transactionId))
        bookItem = datastore.GetBookItem(transaction.GetItemCode())
        borrowDuration = transaction.GetBorrowDuration()
        borrowedOn = transaction.GetBorrowedOn()
        if (dateTool.GetDaysBetween(borrowedOn, dateTool.GetToday()) > borrowDuration):
            sg.Popup("You have exceeded the borrow duration. Please return the book to a library attendant.")
            return False
        transaction.SetReturnedOn(dateTool.GetToday())
        transaction.SetReturned(True)
        bookItem.SetBorrowed(False)
        bookItem.SetBorrower("")
        datastore.SaveData()
        model.transactions = datastore.GetTransactions(model.user.GetUsername(), True)
        model.coverImage = imageTool.MakeSizedImage(datastore.GetImage(), (320, 320))
        model.selectedTransaction = None
        sg.popup("Book returned successfully.")
        self.ModelUpdated(model)
        return False
    
    def table_update(self, row, model):
        if row >= 0 and row < len(model.transactions):
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