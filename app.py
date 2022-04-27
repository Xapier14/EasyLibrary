# App Module
#   Handles the general flow of the application
import PySimpleGUI as sg
import data

controllerStack = []

def PushControllerToStack(controller, model = None):
    global controllerStack
    controllerStack.append(tuple((controller, model)))
    return

def PopControllerFromStack():
    global controllerStack
    return controllerStack.pop()

def PeekControllerFromStack():
    global controllerStack
    return controllerStack[-1]

def HasControllerOnStack():
    global controllerStack
    return len(controllerStack) > 0