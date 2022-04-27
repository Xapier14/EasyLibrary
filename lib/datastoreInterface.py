# DataStoreInterface
#   Defines needed functionality for DataStore implementations

class DataStoreInterface:
    def ReloadData(self):
        raise NotImplementedError("Method not yet implemented.")
    def GetUser(self, username):
        raise NotImplementedError("Method not yet implemented.")
    def GetBook(self, isbn):
        raise NotImplementedError("Method not yet implemented.")
    def GetTransaction(self, id):
        raise NotImplementedError("Method not yet implemented.")