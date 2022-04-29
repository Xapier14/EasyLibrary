# EasyLibrary
# Lance Crisang - 2022

# https://www.github.com/xapier14/EasyLibrary

import data
import app
import make

# Prepare datastore
datastore = data.GetDataStore()

# Prepare initial login controller
app.PushPairToStack(make.MakeLogin(datastore))

# Main program loop
while app.HasControllerOnStack():
    controller, model = app.PeekControllerFromStack()
    controller.Show(model)