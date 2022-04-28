import datetime
import PySimpleGUI as sg
import app
import make
import data

from controller.baseController import Controller

class LoginController(Controller):
    def EventLoop(self, event, values, model):
        if (values != None):
            model.username = values["-username-"]
            model.password = values["-password-"]
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case "OK":
                if (self.button_login(model)):
                    return True
        return False
    
    def Update(self, model):
        self.window["-time-"].update("The time is: " + str(datetime.datetime.now()))
        return

    def button_login(self, model):
        datastore = data.GetDataStore()

        user = datastore.GetUser(model.username)
        if (user == None):
            self.window["-username-"].update("")
            self.window["-password-"].update("")
            sg.Popup("Invalid [username] or password")
            return False
        if (not user.TestPassword(model.password)):
            self.window["-username-"].update("")
            self.window["-password-"].update("")
            sg.Popup("Invalid username or [password]")
            return False
        app.PushPairToStack(make.MakeSelfService(user))
        return True