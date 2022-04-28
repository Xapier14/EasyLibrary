# ControllerBase
#   Defines needed functionality for Controller implementations and default implementations
import PySimpleGUI as sg
from abc import abstractmethod

class Controller:
    def __init__(self, view):
        self.view = view
        self.theme = "DarkBlue17"
        return
    @abstractmethod
    def EventLoop(self, event, values, model):
        raise NotImplementedError("Subclass must implement abstract method")
    def Update(self, model):
        raise NotImplementedError("Subclass must implement abstract method")
    def Show(self, model):
        sg.theme(self.theme)
        self.window = sg.Window(self.view.windowTitle, layout=self.view.ConstructLayout(model), size=(self.view.windowWidth, self.view.windowHeight), finalize=True)
        if (self.view.startMaximized):
            self.window.Maximize()
        # weird fix to force window focus
        self.window.TKroot.focus_force()
        while True:
            event, values = self.window.read(200)
            if self.EventLoop(event, values, model):
                break
            self.Update(model)
        self.window.close()
        return