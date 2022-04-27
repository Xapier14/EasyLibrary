import PySimpleGUI as sg
from controller.controllerInterface import ControllerInterface

class LoginController(ControllerInterface):

    def __init__(self, view):
        self.view = view
        self.windowWidth = 300
        self.windowHeight = 200
        self.windowTitle = "Login"
        self.user = None
        self.loggedIn = False
        return

    def EventLoop(event, values, model):
        if (values != None):
            model.username = values["-username-"]
            model.password = values["-password-"]
        match (event):
            case sg.WIN_CLOSED:
                return True
        return

    def Show(self, model):
        self.window = sg.Window(self.windowTitle, layout=self.view.ConstructLayout(model), size=(self.windowWidth, self.windowHeight))
        while True:
            event, values = self.window.read()
            if LoginController.EventLoop(event, values, model):
                break
        self.window.close()
        return
