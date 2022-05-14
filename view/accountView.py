import PySimpleGUI as sg
from view.viewInterface import ViewInterface

class AccountView(ViewInterface):
    def __init__(self):
        self.windowWidth = 600
        self.windowHeight = 200
        self.windowTitle = "EasyLibrary - Create New User Account"
        self.startMaximized = False
        return
    def ConstructLayout(self, model):
        labelSize = (16, 1)
        frame = [   [sg.Text("Username: ", size=labelSize, justification="right"), sg.Input(model.username, key="-username-", expand_x=True)],
                    [sg.Text("Full Name: ", size=labelSize, justification="right"), sg.Input(model.fullName, key="-fullName-", expand_x=True)],
                    [sg.Text("Password: ", size=labelSize, justification="right"), sg.Input(model.password, password_char="*", key="-password-", expand_x=True)],
                    [sg.Text("Confirm Password: ", size=labelSize, justification="right"), sg.Input(model.confirmPassword, password_char="*", key="-confirmPassword-", expand_x=True)],
                    [sg.VPush()],
                    [sg.Push(), sg.Button("Create Account", key="-button-create-", size=(18, 2))]]
        layout = [ [sg.Frame("Create New User Account", frame, expand_x=True, expand_y=True)] ]
        return layout
    def Update(self, window, model):
        return