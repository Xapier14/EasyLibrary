import data

# models
from model.loginModel import LoginModel
from model.searchModel import SearchModel
from model.selfModel import SelfModel
from model.borrowModel import BorrowModel
from model.returnModel import ReturnModel
# views
from view.loginView import LoginView
from view.searchView import SearchView
from view.selfView import SelfView
from view.borrowView import BorrowView
from view.returnView import ReturnView
# controllers
from controller.loginController import LoginController
from controller.searchController import SearchController
from controller.selfController import SelfController
from controller.borrowController import BorrowController
from controller.returnController import ReturnController


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
    returnModel = ReturnModel(user)
    returnView = ReturnView()
    returnController = ReturnController(returnView)
    return returnController, returnModel