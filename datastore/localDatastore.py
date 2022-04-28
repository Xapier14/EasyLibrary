# LocalDataStore
#   DataStore that functions on a local JSON database.

from datastore.datastoreInterface import DataStoreInterface

class LocalDataStore(DataStoreInterface):
    def __init__(self):
        # Users
        self.Users = []
        # Global Book Data
        self.GlobalBooks = []
        # Local Book Data / Inventory-Stock
        self.LocalBooks = []
        # Transactions (Borrows)
        self.Borrows = []
        # Transactions (Returns)
        self.Returned = []
        return
    
    def GetUser(self, username):
        for user in self.Users:
            if user.GetUsername() == username:
                return user
        return None

    def AddUser(self, user):
        if (self.GetUser(user.GetUsername()) == None):
            self.Users.append(user)
        else:
            return False
        return True