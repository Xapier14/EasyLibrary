from enums import UserEnum
import bcrypt

class User():
    def __init__(self, username = "", level = UserEnum.User, password = "", salt = "", fullName = ""):
        self.__username = username
        self.__hashedPassword = password
        self.__salt = salt
        self.__fullName = fullName
        self.__accessLevel = level

    def GetUsername(self):
        return self.__username

    def GetHashedPassword(self):
        return self.__hashedPassword

    def GetSalt(self):
        return self.__salt

    def GetFullName(self):
        return self.__fullName
    
    def GetAccessLevel(self):
        return self.__accessLevel

    def TestPassword(self, password):
        if (self.__hashedPassword == "" or self.__salt == ""):
            return True
        hash = bcrypt.hashpw(password.encode("utf-8"), self.__salt)
        return hash == self.__hashedPassword

    def SetPassword(self, password):
        self.__salt = bcrypt.gensalt()
        self.__hashedPassword = bcrypt.hashpw(password.encode("utf-8"), self.__salt)
        return