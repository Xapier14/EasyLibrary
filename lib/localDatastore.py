# LocalDataStore
#   DataStore that functions on a local JSON database.

import lib.datastoreInterface as dsi
from lib.datastoreInterface import DataStoreInterface

class LocalDataStore(dsi.DataStoreInterface):
    def __init__(self):
        self.Users = {}
        self.Books = {}
        self.Active = {}
        return
    
    def GetUser(self, username):
        print(f"Getting user '{username}'...")