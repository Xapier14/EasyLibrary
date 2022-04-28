# EasyLibrary
# Lance Crisang - 2022

# https://www.github.com/xapier14/EasyLibrary

import data
import app
import make

from dataModel.user import User
from enums import UserEnum

# Prepare datastore
datastore = data.GetDataStore()

lance = User("lance", UserEnum.User)
lance.SetPassword("12345678")
datastore.AddUser(lance)

# Prepare initial login controller
app.PushPairToStack(make.MakeLogin(datastore))

# Main program loop
while app.HasControllerOnStack():
    controller, model = app.PeekControllerFromStack()
    controller.Show(model)