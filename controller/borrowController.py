from datetime import datetime
import PySimpleGUI as sg
import app
import data
from datamodel.transaction import Transaction
from controller.baseController import Controller

class BorrowController(Controller):
    def EventLoop(self, event, values, model):
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case sg.WIN_X_EVENT:
                if (self.WinClose()):
                    return True
            case "-button-borrow-":
                if (self.button_borrow(model)):
                    return True
            case "-button-retrieve-":
                if (self.button_retrieve(model, values["-item-code-"])):
                    return True
            case "-button-back-":
                if (self.button_back(model)):
                    return True
        return False
        
    def Init(self, model):
        self.borrowDuration = 7 # days
        datastore = data.GetDataStore()
        model.coverImage = datastore.GetImage()
        self.ModelUpdated(model)
        return

    def WinClose(self):
        return False
    
    def Update(self, model):
        return

    def button_borrow(self, model):
        datastore = data.GetDataStore()
        if (model.bookItem is not None):
            borrowDate = datetime.now()
            model.bookItem.SetBorrowed(True)
            model.bookItem.SetBorrower(model.user.GetUsername())
            transactionId = datastore.GetNewTransactionId()
            transaction = Transaction(transactionId, borrowDate, self.borrowDuration, model.bookItem.GetItemCode(), model.user.GetUsername(), False, None)
            model.bookItem.SetLastTransaction(transactionId)
            datastore.AddTransaction(transaction)
            model.canBorrow = False
            self.ModelUpdated(model)
            datastore.SaveData()
            sg.Popup(f"Borrowed successfully.\nPlease return the book within {self.borrowDuration} day(s).")
        return False

    def button_retrieve(self, model, itemCode):
        datastore = data.GetDataStore()
        model.itemCode = itemCode
        model.bookItem = datastore.GetBookItem(int(itemCode)) if (itemCode.isdigit()) else None

        # cannot borrow if book is not available
        model.canBorrow = (model.bookItem is not None)

        # check if book is not available
        if (model.bookItem is not None):
            if (model.bookItem.GetBorrowed()):
                model.canBorrow = False

        # get global book
        if (model.bookItem is not None):
            model.globalBook = datastore.GetBook(model.bookItem.GetISBN())
        
        # get cover image
        if (model.globalBook is not None):
            model.coverImage = datastore.GetImage(model.globalBook.GetISBN())

        # update view
        self.ModelUpdated(model)

        # warn not found item code
        if (model.bookItem is None):
            sg.Popup("Invalid item code")

        return False

    def button_back(self, model):
        app.PopControllerFromStack()
        return True