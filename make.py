# models
from model.loginModel import LoginModel
# views
from view.loginView import LoginView
from view.selfView import SelfView
# controllers
from controller.loginController import LoginController
from controller.selfController import SelfController


def MakeLogin(datastore):
    loginModel = LoginModel(datastore)
    loginView = LoginView()
    loginController = LoginController(loginView)
    return loginController, loginModel

def MakeSelfService():
    selfView = SelfView()
    selfController = SelfController(selfView)
    return selfController, selfView