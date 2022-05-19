from faulthandler import disable
import PySimpleGUI as sg
from view.viewInterface import ViewInterface

class AdminView(ViewInterface):
    def __init__(self):
        self.windowWidth = 1280
        self.windowHeight = 720
        self.windowTitle = "Attended Mode - EasyLibrary"
        self.startMaximized = False
        return
    def ConstructLayout(self, model):
        detailLabelSize = (14, 1)
        buttonSize = (14, 1)

        # Tab 1 : Borrow Books
        borrowBooksValues = []
        borrowBooksColumns = ["Item Code", "Title", "Author", "Publisher", "Year", "Location", "Available?"]
        if len(model.borrowModel.books) > 0:
            borrowBooksValues = model.borrowModel.books
        else:
            borrowBooksValues.append(["No books to show."])
        borrowBooksFrame = [    [sg.Table(values=borrowBooksValues, headings=borrowBooksColumns, expand_x=True, expand_y=True, justification="left", enable_click_events=True, key="-table-borrow-books-")]]
        borrowSearchFrame = [   [sg.Text("Search for Book:"), sg.Input(key="-input-borrow-search-", expand_x=True), sg.Button("Search", key="-button-borrow-search-", size=buttonSize)]]
        borrowDetailsFrame = [  [sg.Text("Item Code:", size=detailLabelSize, justification="right"), sg.Input(key="-input-borrow-itemcode-", disabled=True, expand_x=True)],
                                [sg.Text("Title:", size=detailLabelSize, justification="right"), sg.Input(key="-input-borrow-title-", disabled=True, expand_x=True)],
                                [sg.Text("Author:", size=detailLabelSize, justification="right"), sg.Input(key="-input-borrow-author-", disabled=True, expand_x=True)],
                                [sg.Text("Publisher:", size=detailLabelSize, justification="right"), sg.Input(key="-input-borrow-publisher-", disabled=True, expand_x=True)],
                                [sg.Text("Year:", size=detailLabelSize, justification="right"), sg.Input(key="-input-borrow-year-", disabled=True, expand_x=True)],
                                [sg.Text("Location:", size=detailLabelSize, justification="right"), sg.Input(key="-input-borrow-location-", disabled=True, expand_x=True)],
                                [sg.Text("Available?:", size=detailLabelSize, justification="right"), sg.Input(key="-input-borrow-available-", disabled=True, expand_x=True)]]
        borrowActionsFrame = [  [sg.Text("Username (Borrower):", justification="right"), sg.Input(key="-input-borrow-username-", expand_x=True), sg.Button("Borrow", key="-button-borrow-borrow-", disabled=True, size=buttonSize)]]
        tab1Layout = [  [sg.Frame("Inventory (Books)", borrowBooksFrame, expand_x=True, expand_y=True)],
                        [sg.Frame("Details", borrowDetailsFrame, expand_x=True)],
                        [sg.Frame("Search", borrowSearchFrame, expand_x=True)],
                        [sg.Frame("Actions", borrowActionsFrame, expand_x=True)]
                        ]
        tab1 = sg.Tab("Borrow Books", tab1Layout)

        # Tab 2 : Return Books
        returnBooksValues = []
        returnBooksColumns = ["Transaction ID", "Item Code", "Title", "Author", "Borrowed By", "Borrowed On", "Duration", "Overdue?"]
        if len(model.returnModel.transactions) > 0:
            returnBooksValues = model.returnModel.transactions
        else:
            returnBooksValues.append(["No transactions to show."])
        returnBooksFrame = [    [sg.Table(values=returnBooksValues, headings=returnBooksColumns, expand_x=True, expand_y=True, justification="left", enable_click_events=True, key="-table-return-books-")]]
        returnDetailsFrame = [  [sg.Text("Transaction ID:", size=detailLabelSize, justification="right"), sg.Input(key="-input-return-transactionid-", disabled=True, expand_x=True)],
                                [sg.Text("Item Code:", size=detailLabelSize, justification="right"), sg.Input(key="-input-return-itemcode-", disabled=True, expand_x=True)],
                                [sg.Text("Title:", size=detailLabelSize, justification="right"), sg.Input(key="-input-return-title-", disabled=True, expand_x=True)],
                                [sg.Text("Author:", size=detailLabelSize, justification="right"), sg.Input(key="-input-return-author-", disabled=True, expand_x=True)],
                                [sg.Text("Borrowed By:", size=detailLabelSize, justification="right"), sg.Input(key="-input-return-borrowedby-", disabled=True, expand_x=True)],
                                [sg.Text("Borrowed On:", size=detailLabelSize, justification="right"), sg.Input(key="-input-return-borrowedon-", disabled=True, expand_x=True)],
                                [sg.Text("Duration:", size=detailLabelSize, justification="right"), sg.Input(key="-input-return-duration-", disabled=True, expand_x=True)],
                                [sg.Text("Overdue?:", size=detailLabelSize, justification="right"), sg.Input(key="-input-return-overdue-", disabled=True, expand_x=True)]
                                ]
        returnFilterFrame = [   [sg.Text("Search:", justification="right"), sg.Input(key="-input-return-search-", expand_x=True), sg.Button("Search", key="-button-return-search-", size=buttonSize), sg.Text("Filter by:"), sg.InputCombo(["All", "Overdue", "Not Overdue"], key="-combo-return-filter-", default_value="All", enable_events=True, readonly=True)]]
        tab2Layout = [  [sg.Frame("Active Transactions (For Return)", returnBooksFrame, expand_x=True, expand_y=True)],
                        [sg.Frame("Details", returnDetailsFrame, expand_x=True)],
                        [sg.Frame("Filter", returnFilterFrame, expand_x=True), sg.Button("Return", key="-button-return-return-", disabled=True, size=(14,3))]
                        ]
        tab2 = sg.Tab("Return Books", tab2Layout)

        # Tab 3 : User Accounts
        userAccountsValues = []
        userAccountsColumns = ["Username", "Full Name", "Access Level", "Books Lent", "Total Transactions"]
        if len(model.usersModel.users) > 0:
            userAccountsValues = model.usersModel.users
        else:
            userAccountsValues.append(["No users to show."])
        userAccountsFrame = [    [sg.Table(values=userAccountsValues, headings=userAccountsColumns, expand_x=True, expand_y=True, justification="left", enable_click_events=True, key="-table-user-accounts-")]]
        userFilterFrame = [   [sg.Text("Search:", justification="right"), sg.Input(key="-input-user-search-", expand_x=True), sg.Button("Search", key="-button-user-search-", size=buttonSize), sg.Text("Filter by:"), sg.InputCombo(["All", "Admin", "User"], key="-combo-user-filter-", default_value="All", enable_events=True, readonly=True)]]
        userAccountFrame = [    [sg.Text("Username:", size=detailLabelSize, justification="right"), sg.InputText(key="-input-user-username-", expand_x=True, enable_events=True), sg.Button("Fetch", key="-button-user-fetch-", size=buttonSize)],
                                [sg.Text("Full Name:", size=detailLabelSize, justification="right"), sg.Input(key="-input-user-fullname-", expand_x=True)],
                                [sg.Text("Access Level:", size=detailLabelSize, justification="right"), sg.InputCombo(["Admin", "User"], key="-combo-user-accesslevel-", default_value="User", enable_events=True, readonly=True)],
                                [sg.Text("Password:", size=detailLabelSize, justification="right"), sg.Input(key="-input-user-password-", expand_x=True, password_char="*")],
                                [sg.Push(), sg.Button("Delete", key="-button-user-delete-", disabled=True, size=buttonSize), sg.Button("Create/Update", key="-button-user-create/update-", disabled=True, size=buttonSize)]
                                ]
        tab3Layout = [  [sg.Frame("User Accounts", userAccountsFrame, expand_x=True, expand_y=True)],
                        [sg.Frame("Filter", userFilterFrame, expand_x=True)],
                        [sg.Frame("Account", userAccountFrame, expand_x=True)]
                        ]
        tab3 = sg.Tab("User Accounts", tab3Layout)

        # Tab 4 : Transactions
        transactionsValues = []
        transactionsColumns = ["Transaction ID", "Item Code", "Title", "Author", "Borrowed By", "Borrowed On", "Duration", "Returned On", "Returned?", "Overdue?"]
        if len(model.transactionsModel.transactions) > 0:
            transactionsValues = model.transactionsModel.transactions
        else:
            transactionsValues.append(["No transactions to show."])
        transactionsFrame = [    [sg.Table(values=transactionsValues, headings=transactionsColumns, expand_x=True, expand_y=True, justification="left", enable_click_events=True, key="-table-transactions-")]]
        transactionsDetailsFrame = [  [sg.Text("Transaction ID:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-transactionid-", disabled=True, expand_x=True)],
                                [sg.Text("Item Code:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-itemcode-", disabled=True, expand_x=True)],
                                [sg.Text("Title:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-title-", disabled=True, expand_x=True)],
                                [sg.Text("Author:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-author-", disabled=True, expand_x=True)],
                                [sg.Text("Borrowed By:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-borrowedby-", disabled=True, expand_x=True)],
                                [sg.Text("Borrowed On:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-borrowedon-", disabled=True, expand_x=True)],
                                [sg.Text("Duration:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-duration-", disabled=True, expand_x=True)],
                                [sg.Text("Returned On:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-returnedon-", disabled=True, expand_x=True)],
                                [sg.Text("Returned?:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-returned-", disabled=True, expand_x=True)],
                                [sg.Text("Overdue?:", size=detailLabelSize, justification="right"), sg.Input(key="-input-transactions-overdue-", disabled=True, expand_x=True)]
                                ]
        transactionsFilterFrame = [   [sg.Text("Search:", justification="right"), sg.Input(key="-input-transactions-search-", expand_x=True), sg.Button("Search", key="-button-transactions-search-", size=buttonSize), sg.Text("Filter by:"), sg.InputCombo(["All", "Overdue", "Not Overdue"], key="-combo-transactions-filter-", default_value="All", enable_events=True, readonly=True)]]
        tab4Layout = [  [sg.Frame("Transactions", transactionsFrame, expand_x=True, expand_y=True)],
                        [sg.Frame("Details", transactionsDetailsFrame, expand_x=True)],
                        [sg.Frame("Filter", transactionsFilterFrame, expand_x=True)]
                        ]
        tab4 = sg.Tab("Transactions", tab4Layout)

        # Tab 5 : Global Book Definitions
        globalBookValues = []
        globalBookColumns = ["Title", "Author", "Publisher", "Year", "Genre", "ISBN", "Available", "Inventory Count"]
        if len(model.globalModel.books) > 0:
            globalBookValues = model.globalModel.books
        else:
            globalBookValues.append(["No books to show."])
        globalBookFrame = [    [sg.Table(values=globalBookValues, headings=globalBookColumns, expand_x=True, expand_y=True, justification="left", enable_click_events=True, key="-table-global-")]]
        globalBookNewFrame = [  [sg.Text("ISBN:", size=detailLabelSize, justification="right"), sg.Input(key="-input-global-isbn-", expand_x=True, enable_events=True), sg.Button("Fetch", key="-button-global-fetch-", size=buttonSize)],
                                [sg.Text("Title:", size=detailLabelSize, justification="right"), sg.Input(key="-input-global-title-", expand_x=True)],
                                [sg.Text("Author:", size=detailLabelSize, justification="right"), sg.Input(key="-input-global-author-", expand_x=True)],
                                [sg.Text("Publisher:", size=detailLabelSize, justification="right"), sg.Input(key="-input-global-publisher-", expand_x=True)],
                                [sg.Text("Year:", size=detailLabelSize, justification="right"), sg.Input(key="-input-global-year-", expand_x=True)],
                                [sg.Text("Genre:", size=detailLabelSize, justification="right"), sg.Input(key="-input-global-genre-", expand_x=True)],
                                [sg.Text("Available:", size=detailLabelSize, justification="right"), sg.Input(key="-input-global-available-", expand_x=True, disabled=True)],
                                [sg.Text("Inventory Count:", size=detailLabelSize, justification="right"), sg.Input(key="-input-global-count-", expand_x=True, disabled=True)],
                                [sg.Push(), sg.Button("Create/Update", key="-button-global-create/update-", disabled=True, size=buttonSize)]
                                ]
        globalBookFilterFrame = [   [sg.Text("Search:", justification="right"), sg.Input(key="-input-global-search-", expand_x=True), sg.Button("Search", key="-button-global-search-", size=buttonSize), sg.Text("Filter by:"), sg.InputCombo(["All", "Available", "Not Available"], key="-combo-global-filter-", default_value="All", enable_events=True, readonly=True)]]
        tab5Layout = [  [sg.Frame("Registered Book Data", globalBookFrame, expand_x=True, expand_y=True)],
                        [sg.Frame("Register/Edit Book", globalBookNewFrame, expand_x=True)],
                        [sg.Frame("Filter", globalBookFilterFrame, expand_x=True)]
                        ]
        tab5 = sg.Tab("Global Book Definitions", tab5Layout)

        # Tab 6 : Local Book Inventory
        localBookValues = []
        localBookColumns = [ "Item Code", "ISBN", "Title", "Author", "Location", "Date Added" ]
        if len(model.localModel.books) > 0:
            localBookValues = model.localModel.books
        else:
            localBookValues.append(["No books to show."])
        localBookFrame = [    [sg.Table(values=localBookValues, headings=localBookColumns, expand_x=True, expand_y=True, justification="left", enable_click_events=True, key="-table-local-")]]
        localBookNewFrame = [   [sg.Text("Item Code:", size=detailLabelSize, justification="right"), sg.Input(key="-input-local-itemcode-", expand_x=True, enable_events=True), sg.Button("Fetch", key="-button-local-fetch-", size=buttonSize), sg.Button("Get Free ID", key="-button-local-getfreeid-", size=buttonSize)],
                                [sg.Text("ISBN:", size=detailLabelSize, justification="right"), sg.Input(key="-input-local-isbn-", expand_x=True)],
                                [sg.Text("Title:", size=detailLabelSize, justification="right"), sg.Input(key="-input-local-title-", expand_x=True, disabled=True)],
                                [sg.Text("Author:", size=detailLabelSize, justification="right"), sg.Input(key="-input-local-author-", expand_x=True, disabled=True)],
                                [sg.Text("Location:", size=detailLabelSize, justification="right"), sg.Input(key="-input-local-location-", expand_x=True)],
                                [sg.Text("Date Added:", size=detailLabelSize, justification="right"), sg.Input(key="-input-local-dateadded-", expand_x=True, disabled=True)],
                                [sg.Push(), sg.Button("Create/Update", key="-button-local-create/update-", disabled=True, size=buttonSize)]
                                ]
        localBookFilterFrame = [   [sg.Text("Search:", justification="right"), sg.Input(key="-input-local-search-", expand_x=True), sg.Button("Search", key="-button-local-search-", size=buttonSize)]]
        tab6Layout = [  [sg.Frame("Inventory", localBookFrame, expand_x=True, expand_y=True)],
                        [sg.Frame("Register/Edit Book", localBookNewFrame, expand_x=True)],
                        [sg.Frame("Filter", localBookFilterFrame, expand_x=True)]
                        ]
        tab6 = sg.Tab("Local Book Inventory", tab6Layout)

        tabs = [    [tab1, tab2, tab3, tab4, tab5, tab6]
                    ]
        layout = [  [sg.Text(f"Logged in as {model.user.GetUsername()}"), sg.Push(), sg.Button("Logout", key="-button-logout-", size=(14, 1))],
                    [sg.TabGroup(tabs, expand_x=True, expand_y=True, enable_events=True, key="-tabgroup-")]
                    ]
        return layout
    def Update(self, window, model):
        # Tab 1 : Borrow Books
        if model.updateBorrowModel:
            print("Triggered View Update from Borrow Model")
            model.updateBorrowModel = False
            borrowBooksValues = []
            if len(model.borrowModel.books) > 0:
                borrowBooksValues = model.borrowModel.books
            else:
                borrowBooksValues.append(["No books to show."])
            window["-table-borrow-books-"].update(values=borrowBooksValues)

            window["-button-borrow-borrow-"].update(disabled=not model.borrowModel.canBorrow)
            window["-input-borrow-itemcode-"].update(model.borrowModel.itemCode)
            window["-input-borrow-title-"].update(model.borrowModel.title)
            window["-input-borrow-author-"].update(model.borrowModel.author)
            window["-input-borrow-publisher-"].update(model.borrowModel.publisher)
            window["-input-borrow-year-"].update(model.borrowModel.year)
            window["-input-borrow-location-"].update(model.borrowModel.location)
            window["-input-borrow-available-"].update(model.borrowModel.available)
            if model.borrowModel.clearFilter:
                window["-input-borrow-search-"].update(value="")
                model.borrowModel.clearFilter = False
        # Tab 2 : Return Books
        if model.updateReturnModel:
            print("Triggered View Update from Return Model")
            model.updateReturnModel = False
            returnBooksValues = []
            if len(model.returnModel.transactions) > 0:
                returnBooksValues = model.returnModel.transactions
            else:
                returnBooksValues.append(["No transactions to show."])
            window["-table-return-books-"].update(values=returnBooksValues)

            window["-button-return-return-"].update(disabled=not model.returnModel.canReturn)
            window["-input-return-transactionid-"].update(model.returnModel.transactionId)
            window["-input-return-itemcode-"].update(model.returnModel.itemCode)
            window["-input-return-title-"].update(model.returnModel.title)
            window["-input-return-author-"].update(model.returnModel.author)
            window["-input-return-borrowedby-"].update(model.returnModel.borrowedBy)
            window["-input-return-borrowedon-"].update(model.returnModel.borrowedOn)
            window["-input-return-duration-"].update(model.returnModel.duration)
            window["-input-return-overdue-"].update(model.returnModel.overdue)
        # Tab 3 : Accounts
        if model.updateUsersModel:
            print("Triggered View Update from Users Model")
            model.updateUsersModel = False
            usersValues = []
            if len(model.usersModel.users) > 0:
                usersValues = model.usersModel.users
            else:
                usersValues.append(["No users to show."])
            window["-table-user-accounts-"].update(values=usersValues)
            window["-input-user-username-"].update(model.usersModel.username)
            window["-input-user-fullname-"].update(model.usersModel.fullName)
            window["-combo-user-accesslevel-"].update(model.usersModel.accessLevel)
            window["-button-user-create/update-"].update(disabled=not model.usersModel.canCreateUpdate)
            window["-button-user-delete-"].update(disabled=not model.usersModel.canDelete)
            if model.usersModel.clearPassword:
                window["-input-user-password-"].update(value="")
                model.usersModel.clearPassword = False
        # Tab 4 : Transactions
        if model.updateTransactionsModel:
            print("Triggered View Update from Transactions Model")
            model.updateTransactionsModel = False
            transactionsValues = []
            if len(model.transactionsModel.transactions) > 0:
                transactionsValues = model.transactionsModel.transactions
            else:
                transactionsValues.append(["No transactions to show."])
            window["-table-transactions-"].update(values=transactionsValues)

            window["-input-transactions-transactionid-"].update(model.transactionsModel.transactionId)
            window["-input-transactions-itemcode-"].update(model.transactionsModel.itemCode)
            window["-input-transactions-title-"].update(model.transactionsModel.title)
            window["-input-transactions-author-"].update(model.transactionsModel.author)
            window["-input-transactions-borrowedby-"].update(model.transactionsModel.borrowedBy)
            window["-input-transactions-borrowedon-"].update(model.transactionsModel.borrowedOn)
            window["-input-transactions-duration-"].update(model.transactionsModel.duration)
            window["-input-transactions-returnedon-"].update(model.transactionsModel.returnedOn)
            window["-input-transactions-returned-"].update(model.transactionsModel.returned)
            window["-input-transactions-overdue-"].update(model.transactionsModel.overdue)

        # Tab 5 : Global Book Definitions
        if model.updateGlobalModel:
            print("Triggered View Update from Global Book Model")
            model.updateGlobalModel = False
            globalBooksValues = []
            if len(model.globalModel.books) > 0:
                globalBooksValues = model.globalModel.books
            else:
                globalBooksValues.append(["No books to show."])
            window["-table-global-"].update(values=globalBooksValues)

            window["-input-global-title-"].update(model.globalModel.title)
            window["-input-global-author-"].update(model.globalModel.author)
            window["-input-global-publisher-"].update(model.globalModel.publisher)
            window["-input-global-year-"].update(model.globalModel.year)
            window["-input-global-genre-"].update(model.globalModel.genre)
            window["-input-global-isbn-"].update(model.globalModel.isbn)
            window["-input-global-available-"].update(model.globalModel.available)
            window["-input-global-count-"].update(model.globalModel.count)
            window["-button-global-create/update-"].update(disabled=not model.globalModel.canCreateUpdate)
            if model.globalModel.clearFilter:
                window["-input-global-search-"].update(value="")
                model.globalModel.clearFilter = False

        # Tab 6 : Local Book Definitions
        if model.updateLocalModel:
            print("Triggered View Update from Local Book Model")
            model.updateLocalModel = False
            localBooksValues = []
            if len(model.localModel.books) > 0:
                localBooksValues = model.localModel.books
            else:
                localBooksValues.append(["No books to show."])
            window["-table-local-"].update(values=localBooksValues)

            window["-input-local-itemcode-"].update(model.localModel.itemCode)
            window["-input-local-isbn-"].update(model.localModel.isbn)
            window["-input-local-title-"].update(model.localModel.title)
            window["-input-local-author-"].update(model.localModel.author)
            window["-input-local-location-"].update(model.localModel.location)
            window["-input-local-dateadded-"].update(model.localModel.dateAdded)
            window["-button-local-create/update-"].update(disabled=not model.localModel.canCreateUpdate)
            if model.localModel.clearFilter:
                window["-input-local-search-"].update(value="")
                model.localModel.clearFilter = False
        return