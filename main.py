import data

datastore = data.GetDataStore()
datastore1 = data.GetDataStore()
datastore2 = data.GetDataStore()

datastore.GetUser("lance")

print(datastore)
print(datastore1)
print(datastore2)

print(datastore == datastore1 == datastore2)