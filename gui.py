import PySimpleGUI as sg
import data

from model.loginModel import LoginModel
from view.loginView import LoginView
from controller.loginController import LoginController

controllerStack = []

def MakeLoginController():
    view = LoginView()
    return LoginController(view)

def MakeLoginModel():
    return LoginModel(data.GetDataStore())

def PushControllerToStack(controller):
    global controllerStack
    controllerStack.append(controller)
    return

def PopControllerFromStack():
    global controllerStack
    return controllerStack.pop()