import PySimpleGUI as sg
from view.viewInterface import ViewInterface

class SearchView(ViewInterface):
    def __init__(self):
        self.windowWidth = 1280
        self.windowHeight = 720
        self.windowTitle = "Self-Service Mode - EasyLibrary"
        self.startMaximized = False
        return
    def ConstructLayout(self, model):
        buttonSize = (18, 4)

        bookList = []
        if (len(model.books) > 0):
            for book in model.books:
                bookEntry = [book.GetTitle(), book.GetAuthor(), book.GetISBN(), book.GetYear(), book.GetPublisher()]
                bookList.append(bookEntry)
        else:
            bookList.append(["No books found."])

        listColumn = [[sg.Table(bookList, headings=["Title", "Author", "ISBN", "Year", "Genre", "Publisher"], expand_x=True, expand_y=True) ]]
        detailsColumn = [[sg.Text("details")]]
        layout = [  [sg.Text("EasyLibrary - Self-Service Mode")],
                    [sg.Text("Search for books")],
                    [sg.Column(listColumn, expand_y=True, expand_x=True), sg.Column(detailsColumn, expand_y=True, expand_x=True)],
                    [sg.Push(), sg.Button("Logout", key="-button-logout-", size=buttonSize)] ]
        return layout
    def Update(self, window, model):
        return