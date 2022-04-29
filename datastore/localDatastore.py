# LocalDataStore
#   DataStore that functions on a local JSON database.

import json
import base64
from datamodel.user import User
from datastore.datastoreInterface import DataStoreInterface
from enums import UserEnum

class LocalDataStore(DataStoreInterface):
    def __init__(self):
        self.ReloadData()
        return

    def Prettify(jsonFile):
        f = open(jsonFile, "r")
        userJson = json.load(f)
        f.close()
        f = open(jsonFile, "w")
        json.dump(userJson, f, indent=4)
        f.close()

    def ReloadData(self):
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

        f = open("localDb/users.json", "r")

        users = json.load(f)
        for userEntry in users:
            userType = userEntry["isAdmin"] if UserEnum.Admin else UserEnum.User
            user = User(userEntry["username"], userType, base64.b64decode(bytes(userEntry["password"], "utf-8")), base64.b64decode(bytes(userEntry["salt"], "utf-8")), userEntry["fullName"])
            self.Users.append(user)

        f.close()
        return
    
    def SaveData(self):
        # Write user data
        f = open("localDb/users.json", "w")
        f.write("[")
        for user in self.Users:
            f.write("{")

            f.write("\"username\": \"" + user.GetUsername() + "\",")
            f.write("\"password\": \"" + base64.b64encode(user.GetHashedPassword()).decode("utf-8") + "\",")
            f.write("\"salt\": \"" + base64.b64encode(user.GetSalt()).decode("utf-8") + "\",")
            f.write("\"fullName\": \"" + user.GetFullName() + "\",")
            if user.GetAccessLevel() == UserEnum.Admin:
                f.write("\"isAdmin\": true")
            else:
                f.write("\"isAdmin\": false")

            if user == self.Users[-1]:
                f.write("}")
            else:
                f.write("},")
        f.write("]")
        f.close()
        LocalDataStore.Prettify("localDb/users.json")
        
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
    
    def CountBooks(self):
        return len(self.GlobalBooks)