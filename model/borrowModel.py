class BorrowModel:
    def __init__(self, user = None):
        self.user = user
        self.bookItem = None
        self.globalBook = None
        self.coverImage = ""
        self.itemCode = ""
        self.canBorrow = False