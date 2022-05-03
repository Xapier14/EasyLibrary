# DataStoreInterface
#   Defines needed functionality for DataStore implementations

from abc import abstractmethod

class DataStoreInterface:
    @abstractmethod
    def ReloadData(self):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def SaveData(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def GetUser(self, username):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def AddUser(self, user):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def GetBook(self, isbn):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def AddBook(self, book):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def GetBookItem(self, itemCode):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def GetBookItems(self, isbn):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def AddBookItem(self, book):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def GetTransaction(self, transactionId):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def AddTransaction(self, transaction):
        raise NotImplementedError("Subclass must implement abstract method")
    
    @abstractmethod
    def SearchBooks(self, searchString):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def GetLocations(self, isbn):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def GetNewTransactionId(self):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def CountBookItems(self, isbn):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def CountInventory(self):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def CountBooks(self):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def GetAllBooks(self):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def GetImage(self, isbn):
        raise NotImplementedError("Subclass must implement abstract method")