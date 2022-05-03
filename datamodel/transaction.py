class Transaction:
    def __init__(self, id, borrowedOn, borrowDuration, itemCode, borrower, returned, returnedOn):
        self.__id = id
        self.__borrowedOn = borrowedOn
        self.__borrowDuration = borrowDuration
        self.__itemCode = itemCode
        self.__borrower = borrower
        self.__returned = returned
        self.__returnedOn = returnedOn
    def GetID(self):
        return self.__id
    def GetBorrowedOn(self):
        return self.__borrowedOn
    def GetBorrowDuration(self):
        return self.__borrowDuration
    def GetItemCode(self):
        return self.__itemCode
    def GetBorrower(self):
        return self.__borrower
    def GetReturned(self):
        return self.__returned
    def GetReturnedOn(self):
        return self.__returnedOn
    def SetID(self, id):
        self.__id = id
    def SetBorrowedOn(self, borrowedOn):
        self.__borrowedOn = borrowedOn
    def SetBorrowDuration(self, borrowDuration):
        self.__borrowDuration = borrowDuration
    def SetItemCode(self, itemCode):
        self.__itemCode = itemCode
    def SetBorrower(self, borrower):
        self.__borrower = borrower
    def SetReturned(self, returned):
        self.__returned = returned
    def SetReturnedOn(self, returnedOn):
        self.__returnedOn = returnedOn