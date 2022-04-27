# LocalDataStore
#   DataStore that functions on a local JSON database.

import lib.datastoreInterface as dsi
from lib.datastoreInterface import DataStoreInterface

class LocalDataStore(dsi.DataStoreInterface):
    def __init__(self):
        # Users
        self.Users = {}
        # Global Book Data
        self.GlobalBooks = {}
        # Local Book Data / Inventory-Stock
        self.LocalBooks = {}
        # Transactions (Borrows)
        self.Borrows = {}
        # Transactions (Returns)
        self.Returned = {}
        return
    
    def GetUser(self, username):
        for user in self.Users:
            if user.username == username:
                return user
        return None