class LoginModel:
    def __init__(self, datastore):
        self.username = ""
        self.password = ""
        self.datastore = datastore

    def login(self, username, password):
        user = self.datastore.GetUser(username)
        return user != None