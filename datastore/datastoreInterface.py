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
    def GetBookItem(self, isbn):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def AddBookItem(self, book):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def GetTransactionBorrow(self, id):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def AddTransactionBorrow(self, transaction):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def GetTransactionReturn(self, id):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def AddTransactionReturn(self, transaction):
        raise NotImplementedError("Subclass must implement abstract method")
    def CountBooks(self):
        raise NotImplementedError("Subclass must implement abstract method")