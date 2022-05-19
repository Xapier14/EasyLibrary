class UsersModel:
    def __init__(self):
        self.users = []
        self.username = ""
        self.fullName = ""
        self.accessLevel = "All"
        self.clearPassword = False
        self.canCreateUpdate = False
        self.canDelete = False
        return