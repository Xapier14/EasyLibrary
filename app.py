import PySimpleGUI as sg
import data

# Interfaces
from controller.controllerInterface import ControllerInterface

# Models
from model.loginModel import LoginModel

# Views
from view.loginView import LoginView

# Controllers
from controller.loginController import LoginController

controllerStack = []

def PrepareLogin():
    global controllerStack
    controllerStack = []
    PushControllerToStack(MakeLoginController(), MakeLoginModel())
    return

def MakeLoginController():
    view = LoginView()
    return LoginController(view)

def MakeLoginModel():
    return LoginModel(data.GetDataStore())

def PushControllerToStack(controller, model = None):
    global controllerStack
    controllerStack.append(tuple((controller, model)))
    return

def PopControllerFromStack():
    global controllerStack
    return controllerStack.pop()

def HasControllerOnStack():
    global controllerStack
    return len(controllerStack) > 0