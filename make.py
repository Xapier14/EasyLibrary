import data

# models
from model.loginModel import LoginModel
from model.searchModel import SearchModel
from model.selfModel import SelfModel
from model.borrowModel import BorrowModel
# views
from view.loginView import LoginView
from view.searchView import SearchView
from view.selfView import SelfView
from view.borrowView import BorrowView
# controllers
from controller.loginController import LoginController
from controller.searchController import SearchController
from controller.selfController import SelfController
from controller.borrowController import BorrowController


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