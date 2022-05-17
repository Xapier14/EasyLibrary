class AccountModel:
    def __init__(self):
        self.errorUsernameMsg = ""
        self.errorPasswordMsg = ""
        self.usernameTaken = False
        self.passwordMismatch = True
        self.passwordEmpty = True
        self.username = ""
        self.password = ""
        self.confirmPassword = ""