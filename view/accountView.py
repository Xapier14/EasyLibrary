import PySimpleGUI as sg
from view.viewInterface import ViewInterface

class AccountView(ViewInterface):
    def __init__(self):
        self.windowWidth = 600
        self.windowHeight = 240
        self.windowTitle = "Create New User Account - EasyLibrary"
        self.startMaximized = False
        return
    def ConstructLayout(self, model):
        labelSize = (16, 1)
        frame = [   [sg.Text(model.errorUsernameMsg, key="-error-username-", expand_x=True, justification="center", text_color="red")],
                    [sg.Text("Username: ", size=labelSize, justification="right"), sg.Input("", key="-username-", expand_x=True, enable_events=True)],
                    [sg.Text("Full Name: ", size=labelSize, justification="right"), sg.Input("", key="-fullName-", expand_x=True)],
                    [sg.Text(model.errorPasswordMsg, key="-error-password-", expand_x=True, justification="center", text_color="red")],
                    [sg.Text("Password: ", size=labelSize, justification="right"), sg.Input("", password_char="*", key="-password-", expand_x=True, enable_events=True)],
                    [sg.Text("Confirm Password: ", size=labelSize, justification="right"), sg.Input("", password_char="*", key="-confirmPassword-", expand_x=True, enable_events=True)],
                    [sg.VPush()],
                    [sg.Push(), sg.Button("Create Account", key="-button-create-", size=(18, 2), disabled=model.usernameTaken or model.passwordMismatch)]]
        layout = [ [sg.Frame("Create New User Account", frame, expand_x=True, expand_y=True)] ]
        return layout
    def Update(self, window, model):
        window["-error-username-"].update(model.errorUsernameMsg)
        window["-error-password-"].update(model.errorPasswordMsg)
        window["-button-create-"].update(disabled=model.usernameTaken or model.passwordMismatch)
        return