# ControllerInterface
#   Defines needed functionality for Controller implementations and default implementations
import PySimpleGUI as sg
from abc import abstractmethod

class ControllerInterface:
    def __init__(self, view):
        self.view = view
        return
    @abstractmethod
    def EventLoop(self, event, values, model):
        raise NotImplementedError("Subclass must implement abstract method")
    def Show(self, model):
        self.window = sg.Window(self.view.windowTitle, layout=self.view.ConstructLayout(model), size=(self.view.windowWidth, self.view.windowHeight), finalize=True)
        if (self.view.startMaximized):
            self.window.Maximize()
        while True:
            event, values = self.window.read()
            if self.EventLoop(event, values, model):
                break
        self.window.close()
        return