import PySimpleGUI as sg
import dateTool
from view.viewInterface import ViewInterface

class ReturnView(ViewInterface):
    def __init__(self):
        self.windowWidth = 1280
        self.windowHeight = 720
        self.windowTitle = "Self-Service Mode - EasyLibrary"
        self.startMaximized = False
        return
    def ConstructLayout(self, model):

        # Table Headings: ID, ITEMCODE, TITLE, AUTHOR, BORROWED ON, BORROW DURATION
        tableHeadings = ["Book Title", "Book Author", "Borrowed On", "Borrow Duration", "Item Code"]
        tableData = []
        if len(model.transactions) > 0:
            for transaction in model.transactions:
                globalBook = None
                localBook = None

                for local in model.localBooks:
                    if transaction.GetItemCode() == local.GetItemCode():
                        localBook = local
                        break

                for book in model.globalBooks:
                    if transaction.GetItemCode() == localBook.GetItemCode():
                        globalBook = book
                        break

                tableData.append([globalBook.GetTitle(), globalBook.GetAuthor(), dateTool.DateTimeToString(transaction.GetBorrowedOn()), f"{transaction.GetBorrowDuration()} days", str(transaction.GetItemCode())])
        else:
            tableData.append(["No transactions found."])

        activePanel = [ [sg.Table(tableData, headings=tableHeadings, expand_x=True, expand_y=True, enable_click_events=True, vertical_scroll_only=True, justification="left", num_rows=10, key="-table-")] ]
        leftColumn = [  [sg.Frame("Books Borrowed", activePanel)]]
        layout = [  [sg.Text("EasyLibrary - Self-Service Mode")],
                    [sg.Text("Return a Book")],
                    [sg.Column(leftColumn)] ]
        return layout
    def Update(self, window, model):
        # update table
        tableData = []
        if len(model.transactions) > 0:
            for transaction in model.transactions:
                globalBook = None
                localBook = None

                for local in model.localBooks:
                    if transaction.GetItemCode() == local.GetItemCode():
                        localBook = local
                        break

                for book in model.globalBooks:
                    if transaction.GetItemCode() == localBook.GetItemCode():
                        globalBook = book
                        break

                tableData.append([globalBook.GetTitle(), globalBook.GetAuthor(), dateTool.DateTimeToString(transaction.GetBorrowedOn()), f"{transaction.GetBorrowDuration()} days", str(transaction.GetItemCode())])
        else:
            tableData.append(["No transactions found."])

        print(f"Table: {len(model.transactions)}")

        window["-table-"].update(values=tableData)
        return