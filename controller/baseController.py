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
    @abstractmethod
    def Update(self, model):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def WinClose(self):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def Init(self, model):
        return
    def Show(self, model):
        print("Showing Controller: " + type(self).__name__)
        sg.theme(self.theme)
        self.window = sg.Window(self.view.windowTitle, layout=self.view.ConstructLayout(model), size=(self.view.windowWidth, self.view.windowHeight), finalize=True, enable_close_attempted_event=True)
        if (self.view.startMaximized):
            self.window.Maximize()
        # weird fix to force window focus
        self.window.TKroot.focus_force()
        self.Init(model)
        while True:
            # wait for 200ms for window events.
            # if this receives an event within 200ms, process the event immediately and continue waiting for the next event.
            event, values = self.window.read(200, timeout_key="-timeout-")
            if self.EventLoop(event, values, model) and event != "-timeout-":
                break
            self.Update(model)
        self.window.close()
        print("Controller end.")
        return
    def ModelUpdated(self, model):
        # print(f"[{type(self).__name__}] Model updated. ({type(model).__name__})")
        self.view.Update(self.window, model)
        return