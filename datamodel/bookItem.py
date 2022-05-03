class BookItem:
    def __init__(self, itemCode, isbn, dateAdded, location, borrowed=False, borrower="", lastTransaction=None):
        self.__itemCode = itemCode
        self.__isbn = isbn
        self.__dateAdded = dateAdded
        self.__location = location
        self.__borrowed = borrowed
        self.__borrower = borrower
        self.__lastTransaction = lastTransaction
    def GetItemCode(self):
        return self.__itemCode
    def GetISBN(self):
        return self.__isbn
    def GetDateAdded(self):
        return self.__dateAdded
    def GetLocation(self):
        return self.__location
    def GetBorrowed(self):
        return self.__borrowed
    def GetBorrower(self):
        return self.__borrower
    def GetLastTransaction(self):
        return self.__lastTransaction
    def SetItemCode(self, itemCode):
        self.__itemCode = itemCode
    def SetISBN(self, isbn):
        self.__isbn = isbn
    def SetDateAdded(self, dateAdded):
        self.__dateAdded = dateAdded
    def SetLocation(self, location):
        self.__location = location
    def SetBorrowed(self, borrowed):
        self.__borrowed = borrowed
    def SetBorrower(self, borrower):
        self.__borrower = borrower
    def SetLastTransaction(self, lastTransaction):
        self.__lastTransaction = lastTransaction
    def __str__(self):
        return "Item Code: " + self.__itemCode + "\nISBN: " + self.__isbn + "\nDate Added: " + self.__dateAdded
    def __repr__(self):
        return "Item Code: " + self.__itemCode + "\nISBN: " + self.__isbn + "\nDate Added: " + self.__dateAdded