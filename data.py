import lib.datastore as datastore

__datastoreInstance = None
__datastoreDatabase = "default"

def GetDataStore(database = "default"):
    global __datastoreInstance
    global __datastoreDatabase

    if (__datastoreInstance is None or __datastoreDatabase != database):
        print(f"Creating new instance of DataStore via '{database}'.")
        __datastoreInstance = datastore.DataStore(database)
        __datastoreDatabase = database

    return __datastoreInstance