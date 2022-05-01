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
            case "-button-back-":
                if (self.button_back(model)):
                    return True
            case "-input-query-":
                if (self.input_query(model, values["-input-query-"])):
                    return True
        return False

    def WinClose(self):
        return False
    
    def Update(self, model):
        return

    def button_back(self, model):
        app.PopControllerFromStack()
        return True

    def input_query(self, model, inputText):
        print("Text Updated!")
        model.query = inputText
        model.books = data.GetDataStore().GetAllBooks()
        if (model.query != ""):
            filteredBooks = []
            for book in model.books:
                if (book.GetTitle().lower().find(model.query.lower())!= -1 or book.GetAuthor().lower().find(model.query.lower())!= -1 or book.GetISBN().lower().find(model.query.lower())!= -1):
                    print("Found match!")
                    filteredBooks.append(book)
            model.books = filteredBooks
            print("Books: " + str(len(model.books)))
        self.ModelUpdated(model)
        return False