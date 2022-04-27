# App Module
#   Handles the general flow of the application

controllerStack = []

def PushControllerToStack(controller, model = None):
    global controllerStack
    controllerStack.append(tuple((controller, model)))
    return

def PushPairToStack(tuple):
    global controllerStack
    controllerStack.append(tuple)
    return

def PopControllerFromStack():
    global controllerStack
    return controllerStack.pop()

def PeekControllerFromStack():
    global controllerStack
    return (controllerStack[-1][0], controllerStack[-1][1])

def HasControllerOnStack():
    global controllerStack
    return len(controllerStack) > 0

def ClearControllerStack():
    global controllerStack
    controllerStack.clear()
    return

def GetFirstControllerPairFromStack(controllerType):
    global controllerStack
    for controller, model in controllerStack:
        if (type(controller) == controllerType):
            return controller, model
    return None