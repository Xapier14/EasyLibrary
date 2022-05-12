class ReturnModel:
    def __init__(self, user):
        self.transactions = []
        self.localBooks = []
        self.globalBooks = []
        self.user = user
        self.coverImage = None
        self.selectedTransaction = None