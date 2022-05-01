# Controller for Self-Service search function
import PySimpleGUI as sg
import app
import data
from controller.baseController import Controller

class SearchController(Controller):
    def EventLoop(self, event, values, model):
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case sg.WIN_X_EVENT:
                if (self.WinClose()):
                    return True
            case "-button-clear-":
                if (self.button_clear(model)):
                    return True
            case "-button-back-":
                if (self.button_back(model)):
                    return True
            case "-input-query-":
                model.query = values["-input-query-"]
                self.input_query(model)
        
        # check if event is table event
        if type(event) is tuple:
            if event[0] == "-table-books-" and event[2][0] != None:
                if (event[2][0] >= 0):
                    if (self.table_update(event[2][0], model)):
                        return True
        return False

    def WinClose(self):
        return False
        
    def Init(self, model):
        self.ModelUpdated(model)
        return
    
    def Update(self, model):
        return

    def button_clear(self, model):
        model.selectedBook = None
        self.ModelUpdated(model)
        return False

    def button_back(self, model):
        app.PopControllerFromStack()
        return True

    def input_query(self, model):
        model.books = data.GetDataStore().GetAllBooks()
        model.selectedBook = None
        if (model.query != ""):
            filteredBooks = []
            for book in model.books:
                if (book.GetTitle().lower().find(model.query.lower())!= -1 or book.GetAuthor().lower().find(model.query.lower())!= -1 or book.GetISBN().lower().find(model.query.lower())!= -1 or book.GetYear().lower().find(model.query.lower())!= -1 or book.GetGenre().lower().find(model.query.lower())!= -1 or book.GetPublisher().lower().find(model.query.lower())!= -1):
                    filteredBooks.append(book)
            model.books = filteredBooks
        self.ModelUpdated(model)
        return False

    def table_update(self, row, model):
        if len(model.books) > row:
            model.selectedBook = model.books[row]
        else:
            model.selectedBook = None
        self.ModelUpdated(model)
        return False