class BorrowModel:
    def __init__(self):
        self.books = []
        self.itemCode = ""
        self.title = ""
        self.author = ""
        self.publisher = ""
        self.year = ""
        self.location = ""
        self.available = ""
        self.canBorrow = False
        self.clearFilter = False
        return