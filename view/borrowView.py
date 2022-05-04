import PySimpleGUI as sg
import dateTool
import imageTool
from view.viewInterface import ViewInterface

class BorrowView(ViewInterface):
    def __init__(self):
        self.windowWidth = 1280
        self.windowHeight = 720
        self.windowTitle = "Self-Service Mode - EasyLibrary"
        self.startMaximized = False
        return
    def ConstructLayout(self, model):
        buttonSize = (18, 4)
        detailLabelSize = (10, 1)
        inputFrame = [  [sg.Text("Item Code: ", size=detailLabelSize, justification="right"), sg.InputText(key="-item-code-", enable_events=True, expand_x=True), sg.Button("Retrieve", key="-button-retrieve-", size=buttonSize)]   ]
        detailsFrame = [    [sg.Text("ISBN: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-isbn-", expand_x=True)],
                            [sg.Text("Title: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-title-", expand_x=True)],
                            [sg.Text("Author: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-author-", expand_x=True)],
                            [sg.Text("Publisher: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-publisher-", expand_x=True)],
                            [sg.Text("Year: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-year-", expand_x=True)],
                            [sg.Text("Genre: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-genre-", expand_x=True)],
                            [sg.Text("Item Code: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-itemcode-", expand_x=True)],
                            [sg.Text("Date Added: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-dateadded-", expand_x=True)],
                            [sg.Text("Location: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-location-", expand_x=True)],
                            [sg.Text("Status: ", size=detailLabelSize, justification="right"), sg.InputText("", readonly=True, key="-details-status-", expand_x=True)]
                        ]
        bookCoverFrame = [    [sg.Image(size=(400, 400), key="-image-cover-")]    ]
        actionsFrame = [    [sg.Button("Borrow", key="-button-borrow-", size=buttonSize)]   ]
        leftColumn = [  [sg.Frame("Specify Book Item", inputFrame, expand_x=True)],
                        [sg.Frame("Book Details", detailsFrame, expand_x=True, expand_y=True, element_justification="right")]]
        rightColumn = [ [sg.Frame("Book Cover", bookCoverFrame, expand_x=True, expand_y=True)] ]
        layout = [  [sg.Text("EasyLibrary - Self-Service Mode")],
                    [sg.Text("Borrow a Book")],
                    [sg.Column(leftColumn, expand_x=True, expand_y=True), sg.Column(rightColumn, expand_x=True, expand_y=True)],
                    [sg.Frame("Actions", actionsFrame, expand_x=True), sg.Button("Go Back", key="-button-back-", size=buttonSize)] ]
        return layout
    def Update(self, window, model):
        # change button borrow enable
        window["-button-borrow-"].update(disabled=not model.canBorrow)

        # change book item details
        if (model.bookItem is not None):
            window["-details-isbn-"].update(model.globalBook.GetISBN())
            window["-details-title-"].update(model.globalBook.GetTitle())
            window["-details-author-"].update(model.globalBook.GetAuthor())
            window["-details-publisher-"].update(model.globalBook.GetPublisher())
            window["-details-year-"].update(model.globalBook.GetYear())
            window["-details-genre-"].update(model.globalBook.GetGenre())
            window["-details-itemcode-"].update(str(model.bookItem.GetItemCode()))
            window["-details-dateadded-"].update(dateTool.DateTimeToString(model.bookItem.GetDateAdded()))
            window["-details-location-"].update(model.bookItem.GetLocation())
            window["-details-status-"].update("Available." if not model.bookItem.GetBorrowed() else "Unavailable. (Currently lent to someone)")
        else:
            window["-details-isbn-"].update("")
            window["-details-title-"].update("")
            window["-details-author-"].update("")
            window["-details-publisher-"].update("")
            window["-details-year-"].update("")
            window["-details-genre-"].update("")
            window["-details-itemcode-"].update("")
            window["-details-dateadded-"].update("")
            window["-details-location-"].update("")
            window["-details-status-"].update("")
        
        # change book cover
        if (model.coverImage != ""):
            window["-image-cover-"].update(data=imageTool.MakeSizedImage(model.coverImage, (400, 400)))
        return