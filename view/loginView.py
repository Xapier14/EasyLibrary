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
                                    [sg.Text("The time is: ", key="-time-")],
                                    [sg.Text(f"There are currently {model.bookCount} book(s) registered in the database.", key="-books-")]   ]
                                , key="-left-column-", expand_y=True, expand_x=True, justification="left", element_justification="left")

        rightColumn = sg.Column([   [sg.VPush()],
                                    [sg.Text("Login")],
                                    [sg.Push(), sg.Text("Username: "), sg.InputText(default_text=model.username, key="-username-", size=(30,1), enable_events=True)],
                                    [sg.Push(), sg.Text("Password: "), sg.InputText(default_text=model.password, key="-password-", password_char="*", size=(30,1), enable_events=True)],
                                    [sg.Button("Create Account", key="-button-create-"), sg.Push(), sg.Button("Login as Admin", key="-button-admin-"), sg.Push(), sg.Button("Login as User", key="-button-self-", bind_return_key=True)]   ]
                                , key="-right-column-", expand_y=True, justification="right")
        return [[leftColumn],
                [rightColumn],
                [sg.Text("https://www.github.com/xapier14/EasyLibrary", key="-project-link-", enable_events=True), sg.Push()]]
    
    def Update(self, window, model):
        window["-books-"].update(f"There are currently {model.bookCount} book(s) registered in the database.")
        return