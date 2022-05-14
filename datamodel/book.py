class Book():
    def __init__(self):
        self.__isbn = ""
        self.__title = ""
        self.__author = ""
        self.__publisher = ""
        self.__year = ""
        self.__genre = ""
    def GetISBN(self):
        return self.__isbn
    def GetTitle(self):
        return self.__title
    def GetAuthor(self):
        return self.__author
    def GetPublisher(self):
        return self.__publisher
    def GetYear(self):
        return self.__year
    def GetGenre(self):
        return self.__genre
    def SetISBN(self, isbn):
        self.__isbn = isbn
    def SetTitle(self, title):
        self.__title = title
    def SetAuthor(self, author):
        self.__author = author
    def SetPublisher(self, publisher):
        self.__publisher = publisher
    def SetYear(self, year):
        self.__year = year
    def SetGenre(self, genre):
        self.__genre = genre
    def __str__(self) -> str:
        return f"{self.__title} by {self.__author}"