import PySimpleGUI as sg
from view.viewInterface import ViewInterface

class BorrowView(ViewInterface):
    def __init__(self):
        self.windowWidth = 1280
        self.windowHeight = 720
        self.windowTitle = "Self-Service Mode - EasyLibrary"
        self.startMaximized = False
        return
    def ConstructLayout(self, model):
        layout = [ ]
        return layout
    def Update(self, window, model):
        return