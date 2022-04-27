# Data Module
#   Handles DataStore Singleton Functionality

from argparse import ArgumentError
from datastore.datastoreInterface import DataStoreInterface
from datastore.localDatastore import LocalDataStore

__datastoreInstance = None
__datastoreDatabase = "local"

def GetDataStore(database = "local") -> DataStoreInterface:
    global __datastoreInstance
    global __datastoreDatabase

    if (__datastoreInstance is None):
        print("Creating DataStore Singleton instance...")
        match database:
            case "local":
                __datastoreInstance = LocalDataStore()
                __datastoreDatabase = database
            case "sqlite":
                raise NotImplementedError("SQLite DataStore not yet implemented.")
            case _:
                raise ArgumentError(None, "Unknown DataStore type specified.")
    else:
        print("Reusing DataStore Singleton instance...")

    return __datastoreInstance