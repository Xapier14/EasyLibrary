import PySimpleGUI as sg
from view.viewInterface import ViewInterface

class LoginView(ViewInterface):
    def __init__(self):
        self.windowWidth = 1280
        self.windowHeight = 720
        self.windowTitle = "Login To Account - EasyLibrary"
        self.startMaximized = False
        return

    def ConstructLayout(self, model):
        leftColumn = sg.Column([    [sg.Text("EasyLibrary")],
                                    [sg.Text("The time is: -insert-time-", key="-time-")],
                                    [sg.Text("There are currently {} book(s) registered in the database.")]   ]
                                , key="-left-column-", expand_y=True, expand_x=True, justification="left", element_justification="left")

        rightColumn = sg.Column([   [sg.VPush()],
                                    [sg.Text("Login")],
                                    [sg.Text("Username", size=(10,1)), sg.InputText(default_text=model.username, key="-username-", size=(30,1), enable_events=True)],
                                    [sg.Text("Password", size=(10,1)), sg.InputText(default_text=model.password, key="-password-", password_char="*", size=(30,1), enable_events=True)],
                                    [sg.Push(), sg.Button("OK", key="OK")]]
                                , key="-right-column-", expand_y=True, justification="right")
        return [[leftColumn],
                [rightColumn],
                [sg.Text("Bottom Text")]]
    
    def Update(self, window, model):
        return