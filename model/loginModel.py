class LoginModel:
    def __init__(self, datastore):
        self.username = ""
        self.password = ""
        self.bookCount = datastore.CountBooks()