import PySimpleGUI as sg

import datetime
import webbrowser

import app
import make
import data

from controller.baseController import Controller

class LoginController(Controller):
    def Init(self, model):
        data.GetDataStore().SaveData()
        return
    def EventLoop(self, event, values, model):
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case sg.WIN_X_EVENT:
                if (self.WinClose()):
                    return True
            case "-button-create-":
                if (self.button_create(model)):
                    return True
            case "-button-self-":
                if (self.button_self_login(model)):
                    return True
            case "-button-admin-":
                if (self.button_admin_login(model)):
                    return True
            case "-project-link-":
                if (self.link_projectOpen(model)):
                    return True
            case "-username-":
                model.username = values["-username-"]
            case "-password-":
                model.password = values["-password-"]
        return False
    
    def Update(self, model):
        self.window["-time-"].update("The time is: " + str(datetime.datetime.now()))
        return

    def WinClose(self):
        app.PopControllerFromStack()
        return True

    def link_projectOpen(self, model):
        webbrowser.open("https://www.github.com/xapier14/EasyLibrary")
        return False

    def button_create(self, model):
        app.PushPairToStack(make.MakeCreateAccountService())
        return True

    def button_self_login(self, model):
        datastore = data.GetDataStore()

        user = datastore.GetUser(model.username)
        if (user == None):
            model.username = ""
            model.password = ""
            self.ModelUpdated(model)
            sg.Popup("Invalid username or password")
            return False
        if (not user.TestPassword(model.password)):
            model.username = ""
            model.password = ""
            self.ModelUpdated(model)
            sg.Popup("Invalid username or password")
            return False
        app.PushPairToStack(make.MakeSelfService(user))
        model.username = ""
        model.password = ""
        self.ModelUpdated(model)
        return True

    def button_admin_login(self, model):
        sg.popup("Not implemented yet.")
        return False