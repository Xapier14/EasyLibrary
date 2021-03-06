import PySimpleGUI as sg
from view.viewInterface import ViewInterface

class SelfView(ViewInterface):
    def __init__(self):
        self.windowWidth = 1280
        self.windowHeight = 720
        self.windowTitle = "Self-Service Mode - EasyLibrary"
        self.startMaximized = False
        return
    def ConstructLayout(self, model):
        buttonSize = (22, 4)
        actions = [ sg.Push(),
                    sg.Button("Search for a book", key="-button-search-", size=buttonSize),
                    sg.Button("Borrow a book", key="-button-borrow-", size=buttonSize),
                    sg.Button("Return a book", key="-button-return-", size=buttonSize),
                    sg.Button("View past transactions", key="-button-history-", size=buttonSize),
                    sg.Push() ]
        displayName = model.user.GetUsername() if model.user.GetFullName() == "" else model.user.GetFullName() + f" ({model.user.GetUsername()})"
        layout = [  [sg.Text("EasyLibrary - User View")],
                    [sg.Text(f"Logged in as {displayName}.")],
                    [sg.VPush()],
                    actions,
                    [sg.Push(), sg.Button("Logout", key="-button-logout-", size=buttonSize), sg.Push()],
                    [sg.VPush()] ]
        return layout
    def Update(self, window, model):
        return