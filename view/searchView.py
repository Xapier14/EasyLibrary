import PySimpleGUI as sg
import data
import imageTool
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
                bookEntry = [book.GetTitle(), book.GetAuthor(), book.GetISBN(), book.GetYear(), book.GetGenre(), book.GetPublisher()]
                bookList.append(bookEntry)
        else:
            bookList.append(["No books found."])

        detailBoxSize = (38, 1)
        detailTextSize = (10, 1)
        listColumn = [[sg.Table(bookList, headings=["Title", "Author", "ISBN", "Year", "Genre", "Publisher"], expand_x=True, expand_y=True, enable_click_events=True, vertical_scroll_only=True, justification="left", key="-table-books-") ]]
        detailsFrame = [[sg.Text("Title: ", size=detailTextSize, justification="right"), sg.Input("", readonly=True, size=detailBoxSize, key="-details-title-", expand_x=True)],
                        [sg.Text("Author: ", size=detailTextSize, justification="right"), sg.Input("", readonly=True, size=detailBoxSize, key="-details-author-", expand_x=True)],
                        [sg.Text("ISBN: ", size=detailTextSize, justification="right"), sg.Input("", readonly=True, size=detailBoxSize, key="-details-isbn-", expand_x=True)],
                        [sg.Text("Year: ", size=detailTextSize, justification="right"), sg.Input("", readonly=True, size=detailBoxSize, key="-details-year-", expand_x=True)],
                        [sg.Text("Genre: ", size=detailTextSize, justification="right"), sg.Input("", readonly=True, size=detailBoxSize, key="-details-genre-", expand_x=True)],
                        [sg.Text("Publisher: ", size=detailTextSize, justification="right"), sg.Input("", readonly=True, size=detailBoxSize, key="-details-publisher-", expand_x=True)],
                        [sg.Text("Inventory: ", size=detailTextSize, justification="right"), sg.Input("", readonly=True, size=detailBoxSize, key="-details-inventory-", expand_x=True)],
                        [sg.Text("Status: ", size=detailTextSize, justification="right"), sg.Input("", readonly=True, size=detailBoxSize, key="-details-status-", expand_x=True)],
                        [sg.Text("Location(s): ", size=detailTextSize, justification="right"), sg.Input("", readonly=True, size=detailBoxSize, key="-details-location-", expand_x=True)]]
        imageFrame = [[sg.Image(key="-image-", size=(280, 280))]];
        detailsColumn = [   [sg.Frame("Details", detailsFrame, expand_x=True, element_justification="right")],
                            [sg.Frame("Book Cover", imageFrame, expand_x=True, expand_y=True, element_justification="center", key="-image-frame-")] ]
        layout = [  [sg.Text("EasyLibrary - Self-Service Mode")],
                    [sg.Text("Search for books")],
                    [sg.Column(listColumn, expand_y=True, expand_x=True), sg.Column(detailsColumn, expand_y=True, expand_x=False)],
                    [sg.Text("Search Query: "), sg.Input("", size=(50, 1), key="-input-query-", enable_events=True, expand_x=True), sg.Button("Clear Details", key="-button-clear-", size=buttonSize), sg.Button("Go Back", key="-button-back-", size=buttonSize)] ]
        return layout
    def Update(self, window, model):
        # table update
        bookList = []
        if len(model.books) > 0:
            for book in model.books:
                bookEntry = [book.GetTitle(), book.GetAuthor(), book.GetISBN(), book.GetYear(), book.GetGenre(), book.GetPublisher()]
                bookList.append(bookEntry)
        else:
            bookList.append(["No books found."])
            
        window["-table-books-"].update(values=bookList)

        # details update
        if model.selectedBook is not None:
            datastore = data.GetDataStore()
            window["-details-title-"].update(model.selectedBook.GetTitle())
            window["-details-author-"].update(model.selectedBook.GetAuthor())
            window["-details-isbn-"].update(model.selectedBook.GetISBN())
            window["-details-year-"].update(model.selectedBook.GetYear())
            window["-details-genre-"].update(model.selectedBook.GetGenre())
            window["-details-publisher-"].update(model.selectedBook.GetPublisher())
            window["-details-inventory-"].update(str(datastore.CountBookItems(model.selectedBook.GetISBN())))
            window["-details-status-"].update("")
            window["-details-location-"].update("")
            window["-image-"].update(data=imageTool.MakeSizedImage(datastore.GetImage(model.selectedBook.GetISBN()), (280, 280)))
        else:
            window["-details-title-"].update("")
            window["-details-author-"].update("")
            window["-details-isbn-"].update("")
            window["-details-year-"].update("")
            window["-details-genre-"].update("")
            window["-details-publisher-"].update("")
            window["-details-inventory-"].update("")
            window["-details-status-"].update("")
            window["-details-location-"].update("")
            window["-image-"].update(data=imageTool.MakeSizedImage(data.GetDataStore().GetImage(), (280, 280)))
        return