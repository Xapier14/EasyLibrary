class TransactionsModel:
    def __init__(self, transactionList):
        self.transactionList = transactionList
        self.localBooks = []
        self.globalBooks = []
        return