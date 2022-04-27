import data
import app

# import MVC components
from view.loginView import LoginView
from model.loginModel import LoginModel
from controller.loginController import LoginController

# Prepare datastore
datastore = data.GetDataStore()

# Prepare initial login controller
loginModel = LoginModel(datastore)
loginView = LoginView()
initialLogin = LoginController(loginView)
app.PushControllerToStack(initialLogin, loginModel)

# Main program loop
while app.HasControllerOnStack():
    controller, model = app.PopControllerFromStack()
    controller.Show(model)