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
        buttonSize = (18, 4)
        detailLabelSize = (12, 1)

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
                    if localBook.GetISBN() == book.GetISBN():
                        globalBook = book
                        break

                tableData.append([globalBook.GetTitle(), globalBook.GetAuthor(), dateTool.DateTimeToString(transaction.GetBorrowedOn()), f"{transaction.GetBorrowDuration()} days", str(transaction.GetItemCode())])
        else:
            tableData.append(["No transactions found."])

        activePanel = [ [sg.Table(tableData, headings=tableHeadings, expand_x=True, expand_y=True, enable_click_events=True, vertical_scroll_only=True, justification="left", key="-table-")] ]
        detailsPanel = [    [sg.Text("Transaction ID:", size=detailLabelSize, justification="right"), sg.Input(readonly=True, expand_x=True, key="-transaction-id-", justification="left")],
        [sg.Text("Item Code:", size=detailLabelSize, justification="right"), sg.Input(readonly=True, expand_x=True, key="-item-code-", justification="left")],
        [sg.Text("Book Title:", size=detailLabelSize, justification="right"), sg.Input(readonly=True, expand_x=True, key="-book-title-", justification="left")],
        [sg.Text("Book Author:", size=detailLabelSize, justification="right"), sg.Input(readonly=True, expand_x=True, key="-book-author-", justification="left")],
        [sg.Text("Borrowed On:", size=detailLabelSize, justification="right"), sg.Input(readonly=True, expand_x=True, key="-borrowed-on-", justification="left")],
        [sg.Text("Borrow Duration:", size=detailLabelSize, justification="right"), sg.Input(readonly=True, expand_x=True, key="-borrow-duration-", justification="left")] ]
        coverPanel = [  [sg.VPush()], 
            [ sg.Image(size=(320, 320), background_color="white", key="-image-") ],
            [sg.VPush()] ]
        leftColumn = [  [sg.Frame("Books Borrowed", activePanel, expand_y=True)]]
        rightColumn = [ [sg.Frame("Book Details", detailsPanel, expand_x=True, expand_y=True)] ]
        layout = [  [sg.Text("EasyLibrary - Self-Service Mode")],
                    [sg.Text("Return a Book")],
                    [sg.Column(leftColumn, expand_y=True, expand_x=True), sg.Frame("Book Cover", coverPanel, expand_x=True, expand_y=True, element_justification="center")],
                    [sg.Column(rightColumn, expand_x=True, expand_y=True)],
                    [sg.Button("Return Book", key="-button-return-", size=buttonSize, disabled=True), sg.Push(), sg.Button("Go Back", key="-button-back-", size=buttonSize)] ]
        return layout
    def Update(self, window, model):
        # update details
        if model.selectedTransaction is not None:
            globalBook = None
            localBook = None

            for local in model.localBooks:
                if model.selectedTransaction.GetItemCode() == local.GetItemCode():
                    localBook = local
                    break

            for book in model.globalBooks:
                if model.selectedTransaction.GetItemCode() == localBook.GetItemCode():
                    globalBook = book
                    break

            window["-transaction-id-"].update(str(model.selectedTransaction.GetID()))
            window["-item-code-"].update(str(model.selectedTransaction.GetItemCode()))
            window["-book-title-"].update(globalBook.GetTitle())
            window["-book-author-"].update(globalBook.GetAuthor())
            window["-borrowed-on-"].update(dateTool.DateTimeToString(model.selectedTransaction.GetBorrowedOn()))
            window["-borrow-duration-"].update(f"{model.selectedTransaction.GetBorrowDuration()} days")
            window["-button-return-"].update(disabled=False)
        else:
            window["-transaction-id-"].update("")
            window["-item-code-"].update("")
            window["-book-title-"].update("")
            window["-book-author-"].update("")
            window["-borrowed-on-"].update("")
            window["-borrow-duration-"].update("")
            window["-button-return-"].update(disabled=True)

        # update image
        if model.coverImage is not None:
            window["-image-"].update(data=model.coverImage)

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
                    if localBook.GetISBN() == book.GetISBN():
                        globalBook = book
                        break

                tableData.append([globalBook.GetTitle(), globalBook.GetAuthor(), dateTool.DateTimeToString(transaction.GetBorrowedOn()), f"{transaction.GetBorrowDuration()} days", str(transaction.GetItemCode())])
        else:
            tableData.append(["No transactions found."])

        window["-table-"].update(values=tableData)
        return