import PySimpleGUI as sg
import dateTool
from view.viewInterface import ViewInterface

class TransactionsView(ViewInterface):
    def __init__(self):
        self.windowWidth = 1280
        self.windowHeight = 720
        self.windowTitle = "Self-Service Mode - EasyLibrary"
        self.startMaximized = False
        return
    def ConstructLayout(self, model):
        items = []
        if len(model.transactionList) > 0:
            for transaction in model.transactionList:
                globalBook = None
                localBook = None

                for local in model.localBooks:
                    if transaction.GetItemCode() == local.GetItemCode():
                        localBook = local
                        break

                for book in model.globalBooks:
                    if localBook.GetISBN() == book.GetISBN():
                        globalBook = book
                        break

                items.append([str(transaction.GetItemCode()), globalBook.GetTitle(), globalBook.GetAuthor(), dateTool.DateTimeToString(transaction.GetBorrowedOn()), f"{transaction.GetBorrowDuration()} days", "Not Returned" if (transaction.GetReturnedOn() is None) else dateTool.DateTimeToString(transaction.GetReturnedOn())])
        else:
            items.append(["No transactions found."])
        headings = ["Item Code", "Book Title", "Book Author", "Borrowed On", "Borrow Duration", "Returned On"]
        frame = [ [sg.Table(items, headings=headings, expand_x=True, expand_y=True, justification="left")] ]
        layout = [ [sg.Frame("Past Transactions", frame, expand_x=True, expand_y=True)],
                   [sg.Push(), sg.Button("Go Back", key="-button-back-", size=(18, 4))] ]
        return layout
    def Update(self, window, model):
        return