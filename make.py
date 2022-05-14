import data
import imageTool

# models
from model.loginModel import LoginModel
from model.searchModel import SearchModel
from model.selfModel import SelfModel
from model.borrowModel import BorrowModel
from model.returnModel import ReturnModel
from model.transactionsModel import TransactionsModel
# views
from view.loginView import LoginView
from view.searchView import SearchView
from view.selfView import SelfView
from view.borrowView import BorrowView
from view.returnView import ReturnView
from view.transactionsView import TransactionsView
# controllers
from controller.loginController import LoginController
from controller.searchController import SearchController
from controller.selfController import SelfController
from controller.borrowController import BorrowController
from controller.returnController import ReturnController
from controller.transactionsController import TransactionsController


def MakeLogin(datastore):
    loginModel = LoginModel(datastore)
    loginView = LoginView()
    loginController = LoginController(loginView)
    return loginController, loginModel

def MakeSelfService(user):
    selfModel = SelfModel(user)
    selfView = SelfView()
    selfController = SelfController(selfView)
    return selfController, selfModel

def MakeSearchService():
    datastore = data.GetDataStore()
    searchModel = SearchModel()
    searchModel.books = datastore.GetAllBooks()
    searchView = SearchView()
    searchController = SearchController(searchView)
    return searchController, searchModel

def MakeBorrowService(user):
    borrowModel = BorrowModel(user)
    borrowView = BorrowView()
    borrowController = BorrowController(borrowView)
    return borrowController, borrowModel

def MakeReturnService(user):
    datastore = data.GetDataStore()
    returnModel = ReturnModel(user)
    returnModel.transactions = datastore.GetTransactions(returnModel.user.GetUsername(), True)
    returnModel.globalBooks = datastore.GetAllBooks()
    for transaction in returnModel.transactions:
        returnModel.localBooks.append(datastore.GetBookItem(transaction.GetItemCode()))
    returnModel.coverImage = imageTool.MakeSizedImage(datastore.GetImage(), (320, 320))
    returnView = ReturnView()
    returnController = ReturnController(returnView)
    return returnController, returnModel

def MakeTransactionsService(user):
    datastore = data.GetDataStore()
    transactionsModel = TransactionsModel(datastore.GetTransactions(user.GetUsername()))
    print(f"Transactions: {len(transactionsModel.transactionList)}")
    transactionsModel.globalBooks = datastore.GetAllBooks()
    for transaction in transactionsModel.transactionList:
        transactionsModel.localBooks.append(datastore.GetBookItem(transaction.GetItemCode()))
    transactionsView = TransactionsView()
    transactionsController = TransactionsController(transactionsView)
    return transactionsController, transactionsModel