class BookItem:
    def __init__(self, itemCode, isbn, dateAdded):
        self.__itemCode = itemCode
        self.__isbn = isbn
        self.__dateAdded = dateAdded
    def GetItemCode(self):
        return self.__itemCode
    def GetISBN(self):
        return self.__isbn
    def GetDateAdded(self):
        return self.__dateAdded
    def SetItemCode(self, itemCode):
        self.__itemCode = itemCode
    def SetISBN(self, isbn):
        self.__isbn = isbn
    def SetDateAdded(self, dateAdded):
        self.__dateAdded = dateAdded
    def __str__(self):
        return "Item Code: " + self.__itemCode + "\nISBN: " + self.__isbn + "\nDate Added: " + self.__dateAdded
    def __repr__(self):
        return "Item Code: " + self.__itemCode + "\nISBN: " + self.__isbn + "\nDate Added: " + self.__dateAdded