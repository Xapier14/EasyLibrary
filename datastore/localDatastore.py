# LocalDataStore
#   DataStore that functions on a local JSON database.

import json
import base64
from os.path import exists

# datamodels
from datamodel.user import User
from datamodel.book import Book

# datastore interface
from datastore.datastoreInterface import DataStoreInterface

# user types
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

        # load User Data
        f = open("localDb/users.json", "r")
        users = json.load(f)
        for userEntry in users:
            userType = userEntry["isAdmin"] if UserEnum.Admin else UserEnum.User
            user = User(userEntry["username"], userType, base64.b64decode(bytes(userEntry["password"], "utf-8")), base64.b64decode(bytes(userEntry["salt"], "utf-8")), userEntry["fullName"])
            self.Users.append(user)
        f.close()

        # load Global Book Data
        f = open("localDb/globalBooks.json", "r")
        books = json.load(f)
        for bookEntry in books:
            book = Book()
            book.SetISBN(bookEntry["isbn"])
            book.SetTitle(bookEntry["title"])
            book.SetAuthor(bookEntry["author"])
            book.SetPublisher(bookEntry["publisher"])
            book.SetYear(bookEntry["year"])
            book.SetGenre(bookEntry["genre"])
            self.GlobalBooks.append(book)
        f.close()

        # check default book image
        if not exists("localDb/images/default.png"):
            raise Exception("Default book image not found!")

        return
    
    def SaveData(self):
        # write user data
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
        
        # write global book data
        f = open("localDb/globalBooks.json", "w")
        f.write("[")
        for book in self.GlobalBooks:
            f.write("{")
            f.write("\"isbn\": \"" + book.GetISBN() + "\",")
            f.write("\"title\": \"" + book.GetTitle() + "\",")
            f.write("\"author\": \"" + book.GetAuthor() + "\",")
            f.write("\"publisher\": \"" + book.GetPublisher() + "\",")
            f.write("\"year\": \"" + book.GetYear() + "\",")
            f.write("\"genre\": \"" + book.GetGenre() + "\"")
            if book == self.GlobalBooks[-1]:
                f.write("}")
            else:
                f.write("},")
        f.write("]")
        f.close()
        LocalDataStore.Prettify("localDb/globalBooks.json")

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
    
    def GetBook(self, isbn):
        for book in self.GlobalBooks:
            if book.GetISBN().replace("-", "") == isbn.replace("-", ""):
                return book
        return None
    
    def AddBook(self, book):
        if (self.GetBook(book.GetISBN()) == None):
            self.GlobalBooks.append(book)
        else:
            return False
        return True

    def SearchBooks(self, searchString):
        books = []
        for book in self.GlobalBooks:
            if (book.GetTitle().lower().find(searchString.lower())!= -1 or book.GetAuthor().lower().find(searchString.lower())!= -1 or book.GetISBN().lower().replace("-","").find(searchString.lower().replace("-",""))!= -1 or book.GetYear().lower().find(searchString.lower())!= -1 or book.GetGenre().lower().find(searchString.lower())!= -1 or book.GetPublisher().lower().find(searchString.lower())!= -1):
                books.append(book)
        return books
    
    def CountBooks(self):
        return len(self.GlobalBooks)

    def GetAllBooks(self):
        return self.GlobalBooks

    def GetImage(self, isbn = None):
        if (isbn != None):
            for book in self.GlobalBooks:
                if (book.GetISBN() == isbn):
                    path = "localDb/images/" + book.GetISBN() + ".png"
                    if exists(path):
                        return path
                    elif exists("localDb/images/" + book.GetISBN().replace("-", "") + ".png"):
                        return "localDb/images/" + book.GetISBN().replace("-", "") + ".png"
        return "localDb/images/default.png"