import PySimpleGUI as sg
from view.viewInterface import ViewInterface

class SelfView(ViewInterface):
    def __init__(self):
        self.windowWidth = 1280
        self.windowHeight = 720
        self.windowTitle = "Self-Service Mode - EasyLibrary"
        self.startMaximized = True
        return
    def ConstructLayout(self, model):
        layout = [  [sg.Text("Hello World")],
                    [sg.Text("Logged in as " + model.user.GetUsername())],
                    ]
        return layout
    def Update(self, window, model):
        return