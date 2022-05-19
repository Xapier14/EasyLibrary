# Controller for Admin Window
from glob import glob
from threading import local
import PySimpleGUI as sg
import app
import data
from datamodel.book import Book
from datamodel.bookItem import BookItem
from datamodel.user import User
import dateTool
from enums import UserEnum
from controller.baseController import Controller
from datamodel.transaction import Transaction

class AdminController(Controller):
    def EventLoop(self, event, values, model):
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case sg.WIN_X_EVENT:
                if (self.WinClose()):
                    return True
            case "-button-logout-":
                if (self.button_logout(model)):
                    return True
            case "-tabgroup-":
                match (values["-tabgroup-"]):
                    case "Borrow Books":
                        self.UpdateTab1_Table(model, values["-input-borrow-search-"])
                    case "Return Books":
                        self.UpdateTab2_Table(model, values["-input-return-search-"], values["-combo-return-filter-"])
                    case "User Accounts":
                        self.UpdateTab3_Table(model, values["-input-user-search-"], values["-combo-user-filter-"])
                    case "Transactions":
                        self.UpdateTab4_Table(model, values["-input-transactions-search-"], values["-combo-transactions-filter-"])
                    case "Global Book Definitions":
                        self.UpdateTab5_Table(model, values["-input-global-search-"], values["-combo-global-filter-"])
                    case "Local Book Inventory":
                        self.UpdateTab6_Table(model, values["-input-local-search-"])

            # tab 1
            case "-button-borrow-search-":
                if (self.button_borrow_search(model, values["-input-borrow-search-"])):
                    return True
            case "-button-borrow-borrow-":
                if (self.button_borrow_borrow(model, int(model.borrowModel.itemCode), values["-input-borrow-username-"])):
                    return True

            # tab 2
            case "-button-return-search-":
                if (self.button_return_search(model, values["-input-return-search-"], values["-combo-return-filter-"])):
                    return True
            case "-button-return-return-":
                if (self.button_return_return(model, int(model.returnModel.transactionId), values["-input-return-search-"], values["-combo-return-filter-"])):
                    return True
            case "-combo-return-filter-":
                if (self.combo_return_filter(model, values["-input-return-search-"], values["-combo-return-filter-"])):
                    return True

            # tab 3
            case "-button-user-search-":
                if (self.button_user_search(model, values["-input-user-search-"], values["-combo-user-filter-"])):
                    return True
            case "-button-user-fetch-":
                if (self.button_user_fetch(model, values["-input-user-username-"])):
                    return True
            case "-combo-user-filter-":
                if (self.combo_user_filter(model, values["-input-user-search-"], values["-combo-user-filter-"])):
                    return True
            case "-button-user-create/update-":
                if (self.button_user_create_update(model, values["-input-user-username-"], values["-input-user-fullname-"], values["-combo-user-accesslevel-"], values["-input-user-password-"])):
                    return True
            case "-button-user-delete-":
                if (self.button_user_delete(model, values["-input-user-username-"])):
                    return True
            case "-input-user-username-":
                if (self.input_user_username(model, values["-input-user-username-"])):
                    return True

            # tab 4
            case "-button-transactions-search-":
                if (self.button_transactions_search(model, values["-input-transactions-search-"], values["-combo-transactions-filter-"])):
                    return True
            case "-combo-transactions-filter-":
                if (self.combo_transactions_filter(model, values["-input-transactions-search-"], values["-combo-transactions-filter-"])):
                    return True

            # tab 5
            case "-button-global-search-":
                if (self.button_global_search(model, values["-input-global-search-"], values["-combo-global-filter-"])):
                    return True
            case "-button-global-fetch-":
                if (self.button_global_fetch(model, values["-input-global-isbn-"])):
                    return True
            case "-button-global-create/update-":
                if (self.button_global_create_update(model, values["-input-global-title-"], values["-input-global-author-"], values["-input-global-publisher-"], values["-input-global-year-"], values["-input-global-isbn-"], values["-input-global-genre-"])):
                    return True
            case "-combo-global-filter-":
                if (self.combo_global_filter(model, values["-input-global-search-"], values["-combo-global-filter-"])):
                    return True
            case "-input-global-isbn-":
                if (self.input_global_isbn(model, values["-input-global-isbn-"])):
                    return True

            # tab 6
            case "-button-local-search-":
                if (self.button_local_search(model, values["-input-local-search-"])):
                    return True
            case "-button-local-fetch-":
                if (self.button_local_fetch(model, values["-input-local-itemcode-"])):
                    return True
            case "-button-local-create/update-":
                if (self.button_local_create_update(model, values["-input-local-itemcode-"], values["-input-local-isbn-"], values["-input-local-location-"])):
                    return True
            case "-button-local-getfreeid-":
                if (self.button_local_getfreeid(model)):
                    return True
            case "-input-local-itemcode-":
                if (self.input_local_itemCode(model, values["-input-local-itemcode-"])):
                    return True

        if type(event) is tuple:
            if event[0] == "-table-borrow-books-" and event[2][0] != None:
                if (event[2][0] >= 0):
                    if (self.table_borrow_update(event[2][0], model)):
                        return True
            elif event[0] == "-table-return-books-" and event[2][0] != None:
                if (event[2][0] >= 0):
                    if (self.table_return_update(event[2][0], model)):
                        return True
            elif event[0] == "-table-user-accounts-" and event[2][0] != None:
                if (event[2][0] >= 0):
                    if (self.table_user_update(event[2][0], model)):
                        return True
            elif event[0] == "-table-transactions-" and event[2][0] != None:
                if (event[2][0] >= 0):
                    if (self.table_transactions_update(event[2][0], model)):
                        return True
            elif event[0] == "-table-global-" and event[2][0] != None:
                if (event[2][0] >= 0):
                    if (self.table_global_update(event[2][0], model)):
                        return True
            elif event[0] == "-table-local-" and event[2][0] != None:
                if (event[2][0] >= 0):
                    if (self.table_local_update(event[2][0], model)):
                        return True
        return False

    def Init(self, model):
        datastore = data.GetDataStore()
        # load data into model and submodels
        # tab 1 table
        self.UpdateTab1_Table(model)
        # tab 2 table
        self.UpdateTab2_Table(model)
        # tab 3 table
        self.UpdateTab3_Table(model)
        # tab 4 table
        self.UpdateTab4_Table(model)
        # tab 5 table
        self.UpdateTab5_Table(model)
        # tab 6 table
        self.UpdateTab6_Table(model)
        return

    def UpdateTab1_Table(self, model, filter = ""):
        datastore = data.GetDataStore()
        model.borrowModel.books = []
        for localBook in self.GetFilteredBookItems(filter):
            globalBook = datastore.GetBook(localBook.GetISBN())
            entry = [str(localBook.GetItemCode()), globalBook.GetTitle(), globalBook.GetAuthor(), globalBook.GetPublisher(), globalBook.GetYear(), localBook.GetLocation(), "No" if localBook.GetBorrowed() else "Yes"]
            model.borrowModel.books.append(entry)
        model.borrowModel.itemCode = ""
        model.borrowModel.title = ""
        model.borrowModel.author = ""
        model.borrowModel.publisher = ""
        model.borrowModel.year = ""
        model.borrowModel.location = ""
        model.borrowModel.available = ""
        model.borrowModel.canBorrow = False
        model.borrowModel.clearFilter = True
        self.UpdateBorrowModel(model)

    def UpdateTab2_Table(self, model, searchFilter = "", comboFilter = "All"):
        datastore = data.GetDataStore()
        model.returnModel.transactions = []
        for transaction in datastore.GetTransactions(onlyActive=True):
            daysBetween = dateTool.GetDaysBetween(transaction.GetBorrowedOn(), dateTool.GetToday())
            localBook = datastore.GetBookItem(transaction.GetItemCode())
            globalBook = datastore.GetBook(localBook.GetISBN())
            entry = [str(transaction.GetID()), str(transaction.GetItemCode()), globalBook.GetTitle(), globalBook.GetAuthor(), transaction.GetBorrower(), dateTool.DateTimeToString(transaction.GetBorrowedOn()), str(transaction.GetBorrowDuration()) + " days", "Yes" if daysBetween > 7 else "No"]
            if searchFilter == "" or searchFilter.lower() in globalBook.GetTitle().lower() or searchFilter.lower() in globalBook.GetAuthor().lower() or searchFilter in str(localBook.GetItemCode()) or searchFilter in str(transaction.GetID()) or searchFilter.lower() in transaction.GetBorrower().lower():
                if comboFilter == "All" or (comboFilter == "Overdue" and daysBetween > 7) or (comboFilter == "Not Overdue" and daysBetween <= 7):
                    model.returnModel.transactions.append(entry)
        model.returnModel.transactionId = ""
        model.returnModel.itemCode = ""
        model.returnModel.title = ""
        model.returnModel.author = ""
        model.returnModel.borrowedBy = ""
        model.returnModel.borrowedOn = ""
        model.returnModel.duration = ""
        model.returnModel.overdue = ""
        model.returnModel.canReturn = False
        self.UpdateReturnModel(model)

    def UpdateTab3_Table(self, model, searchFilter = "", comboFilter = "All"):
        datastore = data.GetDataStore()
        model.usersModel.users = []
        for user in datastore.GetAllUsers():
            lent = len(datastore.GetTransactions(user.GetUsername(), onlyActive=True))
            total = len(datastore.GetTransactions(user.GetUsername(), onlyActive=False))
            entry = [user.GetUsername(), user.GetFullName(), "User" if user.GetAccessLevel() == UserEnum.User else "Admin", f"{lent} book(s)", f"{total} book(s)"]
            if searchFilter == "" or searchFilter.lower() in user.GetUsername().lower() or searchFilter.lower() in user.GetFullName().lower():
                if comboFilter == "All" or (comboFilter == "Admin" and user.GetAccessLevel() == UserEnum.Admin) or (comboFilter == "User" and user.GetAccessLevel() == UserEnum.User):
                    model.usersModel.users.append(entry)
        model.usersModel.username = ""
        model.usersModel.fullName = ""
        model.usersModel.accessLevel = "User"
        model.usersModel.clearPassword = True
        self.UpdateUsersModel(model)

    def UpdateTab4_Table(self, model, searchFilter = "", comboFilter = "All"):
        datastore = data.GetDataStore()
        model.transactionsModel.transactions = []
        for transaction in datastore.GetTransactions(onlyActive=False):
            daysBetween = dateTool.GetDaysBetween(transaction.GetBorrowedOn(), dateTool.GetToday())
            localBook = datastore.GetBookItem(transaction.GetItemCode())
            globalBook = datastore.GetBook(localBook.GetISBN())
            entry = [str(transaction.GetID()), str(transaction.GetItemCode()), globalBook.GetTitle(), globalBook.GetAuthor(), transaction.GetBorrower(), dateTool.DateTimeToString(transaction.GetBorrowedOn()), str(transaction.GetBorrowDuration()) + " days", dateTool.DateTimeToString(transaction.GetReturnedOn()), "Yes" if transaction.GetReturned() else "No", "Yes" if daysBetween > 7 else "No"]
            if searchFilter == "" or searchFilter.lower() in globalBook.GetTitle().lower() or searchFilter.lower() in globalBook.GetAuthor().lower() or searchFilter in str(localBook.GetItemCode()) or searchFilter in str(transaction.GetID()) or searchFilter.lower() in transaction.GetBorrower().lower():
                if comboFilter == "All" or (comboFilter == "Overdue" and daysBetween > 7) or (comboFilter == "Not Overdue" and daysBetween <= 7):
                    model.transactionsModel.transactions.append(entry)
        model.transactionsModel.transactionId = ""
        model.transactionsModel.itemCode = ""
        model.transactionsModel.title = ""
        model.transactionsModel.author = ""
        model.transactionsModel.borrowedBy = ""
        model.transactionsModel.borrowedOn = ""
        model.transactionsModel.returnedOn = ""
        model.transactionsModel.duration = ""
        model.transactionsModel.overdue = ""
        model.transactionsModel.returned = ""
        self.UpdateTransactionsModel(model)

    def UpdateTab5_Table(self, model, searchFilter = "", comboFilter = "All"):
        datastore = data.GetDataStore()
        model.globalModel.books = []
        for book in datastore.GetAllBooks():
            available = len(datastore.GetBookItems(book.GetISBN(), onlyAvailable=True))
            total = len(datastore.GetBookItems(book.GetISBN()))
            entry = [book.GetTitle(), book.GetAuthor(), book.GetPublisher(), book.GetYear(), book.GetGenre(), book.GetISBN(), str(available) + " copie(s)", str(total) + " copie(s)"]
            if searchFilter == "" or searchFilter.lower() in book.GetTitle().lower() or searchFilter.lower() in book.GetAuthor().lower() or searchFilter in str(book.GetISBN()) or searchFilter in book.GetYear() or searchFilter.lower() in book.GetPublisher().lower() or searchFilter.lower() in book.GetGenre().lower():
                if comboFilter == "All" or (comboFilter == "Available" and available > 0) or (comboFilter == "Not Available" and available == 0):
                    model.globalModel.books.append(entry)
        model.globalModel.title = ""
        model.globalModel.author = ""
        model.globalModel.publisher = ""
        model.globalModel.year = ""
        model.globalModel.genre = ""
        model.globalModel.isbn = ""
        model.globalModel.available = ""
        model.globalModel.count = ""
        model.globalModel.canCreateUpdate = False
        self.UpdateGlobalModel(model)

    def UpdateTab6_Table(self, model, searchFilter = ""):
        datastore = data.GetDataStore()
        model.localModel.books = []
        for book in datastore.GetAllInventory():
            globalBook = datastore.GetBook(book.GetISBN())
            entry = [book.GetItemCode(), book.GetISBN(), globalBook.GetTitle(), globalBook.GetAuthor(), book.GetLocation(), dateTool.DateTimeToString(book.GetDateAdded())]
            if searchFilter == "" or searchFilter.lower() in globalBook.GetTitle().lower() or searchFilter.lower() in globalBook.GetAuthor().lower() or searchFilter in str(book.GetItemCode()) or searchFilter in book.GetISBN() or searchFilter.lower() in book.GetLocation().lower():
                model.localModel.books.append(entry)
        model.localModel.itemCode = ""
        model.localModel.isbn = ""
        model.localModel.title = ""
        model.localModel.author = ""
        model.localModel.location = ""
        model.localModel.dateAdded = ""
        model.localModel.canCreateUpdate = False
        self.UpdateLocalModel(model)

    def WinClose(self):
        return False
    
    def Update(self, model):
        return
        
    def button_logout(self, model):
        datastore = data.GetDataStore()
        datastore.SaveData()
        app.PopControllerFromStack()
        return True

    # tab 1
    def table_borrow_update(self, index, model):
        if index >= 0 and index < len(model.borrowModel.books):
            model.borrowModel.itemCode = model.borrowModel.books[index][0]
            model.borrowModel.title = model.borrowModel.books[index][1]
            model.borrowModel.author = model.borrowModel.books[index][2]
            model.borrowModel.publisher = model.borrowModel.books[index][3]
            model.borrowModel.year = model.borrowModel.books[index][4]
            model.borrowModel.location = model.borrowModel.books[index][5]
            model.borrowModel.available = model.borrowModel.books[index][6]
            model.borrowModel.canBorrow = True if model.borrowModel.available == "Yes" else False
            self.UpdateBorrowModel(model)
        return False

    def button_borrow_search(self, model, searchFilter = ""):
        self.UpdateTab1_Table(model, searchFilter)
        return False

    def button_borrow_borrow(self, model, itemCode, username):
        datastore = data.GetDataStore()
        user = datastore.GetUser(username)
        if user == None:
            sg.Popup("User not found.")
            return False
        localBook = datastore.GetBookItem(itemCode)
        if localBook.GetBorrowed():
            sg.Popup("Book is already borrowed.")
            return False
        # create transaction
        localBook.SetBorrowed(True)
        localBook.SetBorrower(username)
        transactionId = datastore.GetNewTransactionId()
        transaction = Transaction(transactionId, dateTool.GetToday(), 7, itemCode, username, False, None)
        localBook.SetLastTransaction(transactionId)
        datastore.AddTransaction(transaction)
        datastore.SaveData()
        self.UpdateTab1_Table(model, "")
        sg.Popup("Book borrowed for 7 days.")
        return False

    # tab 2
    def table_return_update(self, index, model):
        if index >= 0 and index < len(model.returnModel.transactions):
            model.returnModel.transactionId = model.returnModel.transactions[index][0]
            model.returnModel.itemCode = model.returnModel.transactions[index][1]
            model.returnModel.title = model.returnModel.transactions[index][2]
            model.returnModel.author = model.returnModel.transactions[index][3]
            model.returnModel.borrowedBy = model.returnModel.transactions[index][4]
            model.returnModel.borrowedOn = model.returnModel.transactions[index][5]
            model.returnModel.duration = model.returnModel.transactions[index][6]
            model.returnModel.overdue = model.returnModel.transactions[index][7]
            model.returnModel.canReturn = True
            self.UpdateReturnModel(model)
        return False

    def button_return_search(self, model, searchFilter = "", comboFilter = "All"):
        self.UpdateTab2_Table(model, searchFilter, comboFilter)
        return False

    def button_return_return(self, model, transactionId, searchFilter = "", comboFilter = "All"):
        datastore = data.GetDataStore()
        transaction = datastore.GetTransaction(transactionId)
        if transaction == None:
            sg.Popup("Transaction not found.")
            return False
        localBook = datastore.GetBookItem(transaction.GetItemCode())
        localBook.SetBorrowed(False)
        localBook.SetBorrower("")
        transaction.SetReturned(True)
        transaction.SetReturnedOn(dateTool.GetToday())
        datastore.SaveData()
        self.UpdateTab2_Table(model, searchFilter, comboFilter)
        sg.Popup("Book returned.")
        return False

    def combo_return_filter(self, model, searchFilter, comboFilter):
        self.UpdateTab2_Table(model, searchFilter, comboFilter)
        return False

    # tab 3
    def table_user_update(self, index, model):
        if index >= 0 and index < len(model.usersModel.users):
            model.usersModel.username = model.usersModel.users[index][0]
            model.usersModel.fullName = model.usersModel.users[index][1]
            model.usersModel.accessLevel = model.usersModel.users[index][2]
            model.usersModel.clearPassword = True
            model.usersModel.canDelete = True
            model.usersModel.canCreateUpdate = True
            self.UpdateUsersModel(model)
        return False

    def button_user_search(self, model, searchFilter = "", comboFilter = "All"):
        self.UpdateTab3_Table(model, searchFilter, comboFilter)
        return False

    def button_user_fetch(self, model, username):
        datastore = data.GetDataStore()
        user = datastore.GetUser(username)
        if user == None:
            sg.Popup("User not found.")
            return False
        model.usersModel.username = user.GetUsername()
        model.usersModel.fullName = user.GetFullName()
        model.usersModel.accessLevel = "User" if user.GetAccessLevel() == UserEnum.User else "Admin"
        model.usersModel.clearPassword = True
        model.usersModel.canDelete = True
        model.usersModel.canCreateUpdate = True
        self.UpdateUsersModel(model)
        return False

    def combo_user_filter(self, model, searchFilter, comboFilter):
        self.UpdateTab3_Table(model, searchFilter, comboFilter)
        return False

    def button_user_create_update(self, model, username, fullName, accessLevel, password = ""):
        datastore = data.GetDataStore()
        if username == "":
            sg.Popup("Username is required.")
            return False
        if fullName == "":
            sg.Popup("Full name is required.")
            return False
        if accessLevel == "":
            sg.Popup("Access level is required.")
            return False
        user = datastore.GetUser(username)
        if user == None:
            user = User(username, UserEnum.User if accessLevel == "User" else UserEnum.Admin, fullName=fullName)
            user.SetPassword(password)
            datastore.AddUser(user)
            sg.Popup("User created.")
        else:
            user.SetFullName(fullName)
            user.SetAccessLevel(UserEnum.User if accessLevel == "User" else UserEnum.Admin)
            if password != "":
                user.SetPassword(password)
            sg.Popup("User updated.")
        datastore.SaveData()
        model.usersModel.canCreateUpdate = False
        self.UpdateTab3_Table(model, "", "All")
        return False

    def button_user_delete(self, model, username):
        datastore = data.GetDataStore()
        user = datastore.GetUser(username)
        if user == None:
            sg.Popup("User not found.")
            return False
        if len(datastore.GetTransactions(username, True)) > 0:
            sg.Popup("User cannot be deleted. Active transactions exist.")
            return False
        datastore.RemoveUser(username)
        datastore.SaveData()
        self.UpdateTab3_Table(model, "", "All")
        sg.Popup("User deleted.")
        return False

    def input_user_username(self, model, username):
        model.usersModel.username = username
        model.usersModel.fullName = ""
        model.usersModel.accessLevel = "User"
        model.usersModel.clearPassword = True
        model.usersModel.canCreateUpdate = username != ""
        model.usersModel.canDelete = False
        self.UpdateUsersModel(model)
        return False

    # tab 4
    def table_transactions_update(self, index, model):
        if index >= 0 and index < len(model.transactionsModel.transactions):
            model.transactionsModel.transactionId = model.transactionsModel.transactions[index][0]
            model.transactionsModel.itemCode = model.transactionsModel.transactions[index][1]
            model.transactionsModel.title = model.transactionsModel.transactions[index][2]
            model.transactionsModel.author = model.transactionsModel.transactions[index][3]
            model.transactionsModel.borrowedBy = model.transactionsModel.transactions[index][4]
            model.transactionsModel.borrowedOn = model.transactionsModel.transactions[index][5]
            model.transactionsModel.duration = model.transactionsModel.transactions[index][6]
            model.transactionsModel.returnedOn = model.transactionsModel.transactions[index][7]
            model.transactionsModel.returned = model.transactionsModel.transactions[index][8]
            model.transactionsModel.overdue = model.transactionsModel.transactions[index][9]
            self.UpdateTransactionsModel(model)
        return False
    
    def button_transactions_search(self, model, searchFilter = "", comboFilter = "All"):
        self.UpdateTab4_Table(model, searchFilter, comboFilter)
        return False

    def combo_transactions_filter(self, model, searchFilter = "", comboFilter = "All"):
        self.UpdateTab4_Table(model, searchFilter, comboFilter)
        return False

    # tab 5
    def table_global_update(self, index, model):
        if index >= 0 and index < len(model.globalModel.books):
            model.globalModel.title = model.globalModel.books[index][0]
            model.globalModel.author = model.globalModel.books[index][1]
            model.globalModel.publisher = model.globalModel.books[index][2]
            model.globalModel.year = model.globalModel.books[index][3]
            model.globalModel.genre = model.globalModel.books[index][4]
            model.globalModel.isbn = model.globalModel.books[index][5]
            model.globalModel.available = model.globalModel.books[index][6]
            model.globalModel.count = model.globalModel.books[index][7]
            model.globalModel.canCreateUpdate = True
            self.UpdateGlobalModel(model)
        return False

    def button_global_search(self, model, searchFilter = "", comboFilter = "All"):
        self.UpdateTab5_Table(model, searchFilter, comboFilter)
        return False

    def button_global_fetch(self, model, isbn):
        datastore = data.GetDataStore()
        book = datastore.GetBook(isbn)
        if book == None:
            sg.Popup("Book not found.")
            return False
        available = len(datastore.GetBookItems(book.GetISBN(), onlyAvailable=True))
        total = len(datastore.GetBookItems(book.GetISBN()))
        model.globalModel.title = book.GetTitle()
        model.globalModel.author = book.GetAuthor()
        model.globalModel.publisher = book.GetPublisher()
        model.globalModel.year = book.GetYear()
        model.globalModel.isbn = book.GetISBN()
        model.globalModel.available = f"{available} copie(s)"
        model.globalModel.count = f"{total} copie(s)"
        model.globalModel.canCreateUpdate = True
        self.UpdateGlobalModel(model)
        return False

    def button_global_create_update(self, model, title, author, publisher, year, isbn, genre):
        datastore = data.GetDataStore()
        book = datastore.GetBook(isbn)
        if book == None:
            book = Book()
            book.SetISBN(isbn)
            book.SetTitle(title)
            book.SetAuthor(author)
            book.SetPublisher(publisher)
            book.SetYear(year)
            book.SetGenre(genre)
            datastore.AddBook(book)
            sg.Popup("Book created.")
        else:
            book.SetTitle(title)
            book.SetAuthor(author)
            book.SetPublisher(publisher)
            book.SetYear(year)
            book.SetGenre(genre)
            sg.Popup("Book updated.")
        datastore.SaveData()
        model.globalModel.canCreateUpdate = False
        model.globalModel.clearFilter = True
        self.UpdateTab5_Table(model, "", "All")
        return False

    def combo_global_filter(self, model, searchFilter = "", comboFilter = "All"):
        self.UpdateTab5_Table(model, searchFilter, comboFilter)
        return False

    def input_global_isbn(self, model, isbn):
        model.globalModel.isbn = isbn
        model.globalModel.title = ""
        model.globalModel.author = ""
        model.globalModel.publisher = ""
        model.globalModel.year = ""
        model.globalModel.genre = ""
        model.globalModel.available = ""
        model.globalModel.count = ""
        model.globalModel.canCreateUpdate = isbn != ""
        self.UpdateGlobalModel(model)
        return False

    # tab 6
    def table_local_update(self, index, model):
        if index >= 0 and index < len(model.localModel.books):
            model.localModel.itemCode = model.localModel.books[index][0]
            model.localModel.isbn = model.localModel.books[index][1]
            model.localModel.title = model.localModel.books[index][2]
            model.localModel.author = model.localModel.books[index][3]
            model.localModel.location = model.localModel.books[index][4]
            model.localModel.dateAdded = model.localModel.books[index][5]
            model.localModel.canCreateUpdate = True
            self.UpdateLocalModel(model)
        return False

    def button_local_search(self, model, searchFilter = ""):
        self.UpdateTab6_Table(model, searchFilter)
        return False

    def button_local_fetch(self, model, itemCode):
        datastore = data.GetDataStore()
        item = datastore.GetBookItem(int(itemCode))
        if item == None:
            sg.Popup("Item not found.")
            return False
        book = datastore.GetBook(item.GetISBN())
        if book == None:
            sg.Popup("Book not found.")
            return False
        model.localModel.itemCode = item.GetItemCode()
        model.localModel.isbn = item.GetISBN()
        model.localModel.title = book.GetTitle()
        model.localModel.author = book.GetAuthor()
        model.localModel.location = item.GetLocation()
        model.localModel.dateAdded = item.GetDateAdded()
        model.localModel.canCreateUpdate = True
        self.UpdateLocalModel(model)
        return False

    def button_local_create_update(self, model, itemCode, isbn, location):
        datastore = data.GetDataStore()
        item = datastore.GetBookItem(int(itemCode))
        if datastore.GetBook(isbn) == None:
            sg.Popup("Global book definition not found.")
            return False
        if location == "":
            sg.Popup("Location not specified.")
            return False
        if item == None:
            item = BookItem(itemCode, isbn, dateTool.GetToday(), location)
            datastore.AddBookItem(item)
            sg.Popup("Item created.")
        else:
            item.SetLocation(location)
            sg.Popup("Item updated.")
        datastore.SaveData()
        model.localModel.canCreateUpdate = False
        model.localModel.clearFilter = True
        self.UpdateTab6_Table(model, "")
        return False

    def button_local_getfreeid(self, model):
        datastore = data.GetDataStore()
        model.localModel.itemCode = datastore.GetNewItemCode()
        model.localModel.canCreateUpdate = True
        self.UpdateLocalModel(model)
        return False

    def input_local_itemCode(self, model, itemCode):
        model.localModel.itemCode = itemCode
        model.localModel.isbn = ""
        model.localModel.title = ""
        model.localModel.author = ""
        model.localModel.location = ""
        model.localModel.dateAdded = ""
        model.localModel.canCreateUpdate = itemCode != ""
        self.UpdateLocalModel(model)
        return False

    def UpdateBorrowModel(self, model):
        model.updateBorrowModel = True
        self.ModelUpdated(model)
        return

    def UpdateReturnModel(self, model):
        model.updateReturnModel = True
        self.ModelUpdated(model)
        return
    
    def UpdateTransactionsModel(self, model):
        model.updateTransactionsModel = True
        self.ModelUpdated(model)
        return
    
    def UpdateUsersModel(self, model):
        model.updateUsersModel = True
        self.ModelUpdated(model)
        return
    
    def UpdateLocalModel(self, model):
        model.updateLocalModel = True
        self.ModelUpdated(model)
        return

    def UpdateGlobalModel(self, model):
        model.updateGlobalModel = True
        self.ModelUpdated(model)

    def UpdateAllModels(self, model):
        model.updateBorrowModel = True
        model.updateReturnModel = True
        model.updateTransactionsModel = True
        model.updateUsersModel = True
        model.updateLocalMOdel = True
        model.updateGlobalModel = True
        self.ModelUpdated(model)
        return

    def GetFilteredBookItems(self, filter = ""):
        filteredBooks = []
        datastore = data.GetDataStore()
        if filter == "":
            return datastore.GetAllInventory()
        for localBook in datastore.GetAllInventory():
            globalBook = datastore.GetBook(localBook.GetISBN())
            if globalBook.GetTitle().lower().find(filter.lower()) != -1 or globalBook.GetAuthor().lower().find(filter.lower()) != -1 or globalBook.GetPublisher().lower().find(filter.lower()) != -1 or globalBook.GetYear().lower().find(filter.lower()) != -1 or str(localBook.GetItemCode()).lower().find(filter.lower()) != -1 or localBook.GetLocation().lower().find(filter.lower()) != -1:
                filteredBooks.append(localBook)
        return filteredBooks