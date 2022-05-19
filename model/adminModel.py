from model.submodel.borrowModel import BorrowModel
from model.submodel.returnModel import ReturnModel
from model.submodel.transactionsModel import TransactionsModel
from model.submodel.usersModel import UsersModel
from model.submodel.localModel import LocalModel
from model.submodel.globalModel import GlobalModel

class AdminModel:
    def __init__(self, user):
        self.user = user
        self.borrowModel = BorrowModel()
        self.updateBorrowModel = False
        self.returnModel = ReturnModel()
        self.updateReturnModel = False
        self.transactionsModel = TransactionsModel()
        self.updateTransactionsModel = False
        self.usersModel = UsersModel()
        self.updateUsersModel = False
        self.localModel = LocalModel()
        self.updateLocalModel = False
        self.globalModel = GlobalModel()
        self.updateGlobalModel = False