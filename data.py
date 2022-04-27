# Data Module
#   Handles DataStore Singleton Functionality

from argparse import ArgumentError
import lib.datastoreInterface as dsi
import lib.localDatastore as localDatastore

__datastoreInstance = None
__datastoreDatabase = "local"

def GetDataStore(database = "local") -> dsi.DataStoreInterface:
    global __datastoreInstance
    global __datastoreDatabase

    if (__datastoreInstance is None):
        print("Creating DataStore Singleton instance...")
        match database:
            case "local":
                __datastoreInstance = localDatastore.LocalDataStore()
                __datastoreDatabase = database
            case "sqlite":
                raise NotImplementedError("SQLite DataStore not yet implemented.")
            case _:
                raise ArgumentError(None, "Unknown DataStore type specified.")
    else:
        print("Reusing DataStore Singleton instance...")

    return __datastoreInstance