# Controller for Account Creation
import PySimpleGUI as sg
import app
import data
from controller.baseController import Controller
import datamodel.user

class AccountController(Controller):
    def EventLoop(self, event, values, model):
        match (event):
            case sg.WIN_CLOSED:
                app.PopControllerFromStack()
                return True
            case sg.WIN_X_EVENT:
                if (self.WinClose()):
                    return True
            case "-username-":
                if (self.UsernameTextbox_Updated(model, values["-username-"])):
                    return True
            case "-password-":
                if (self.PasswordTextbox_Updated(model, values["-password-"])):
                    return True
            case "-confirmPassword-":
                if (self.ConfirmPasswordTextbox_Updated(model, values["-confirmPassword-"])):
                    return True
            case "-button-create-":
                if (self.button_create(model, values["-fullName-"])):
                    return True
        return False

    def Init(self, model):
        return

    def WinClose(self):
        app.PopControllerFromStack()
        return True
    
    def Update(self, model):
        self.CheckUsernameAvailability(model)
        self.CheckPasswordMatching(model)
        self.CheckPasswordEmpty(model)
        # update error message
        if model.usernameTaken:
            model.errorUsernameMsg = "Username is taken or empty"
        else:
            model.errorUsernameMsg = ""
        if model.passwordEmpty:
            model.errorPasswordMsg = "Password is empty"
        elif model.passwordMismatch:
            model.errorPasswordMsg = "Passwords do not match"
        else:
            model.errorPasswordMsg = ""
        return

    def UsernameTextbox_Updated(self, model, text):
        model.username = text
        return False
        
    def PasswordTextbox_Updated(self, model, text):
        model.password = text
        return False
        
    def ConfirmPasswordTextbox_Updated(self, model, text):
        model.confirmPassword = text
        return False

    def CheckUsernameAvailability(self, model):
        datastore = data.GetDataStore()
        if (datastore.GetUser(model.username) != None or model.username == ""):
            model.usernameTaken = True
        else:
            model.usernameTaken = False
        self.ModelUpdated(model)
        return

    def CheckPasswordMatching(self, model):
        if (model.password == model.confirmPassword and model.password != ""):
            model.passwordMismatch = False
        else:
            model.passwordMismatch = True
        self.ModelUpdated(model)
        return

    def CheckPasswordEmpty(self, model):
        if (model.password == ""):
            model.passwordEmpty = True
        else:
            model.passwordEmpty = False
        self.ModelUpdated(model)
        return
    
    def button_create(self, model, fullName):
        datastore = data.GetDataStore()
        user = datastore.GetUser(model.username)
        if (user != None):
            model.usernameTaken = True
            self.ModelUpdated(model)
            sg.Popup("Username is taken")
            return False
        if (model.password == ""):
            model.passwordEmpty = True
            self.ModelUpdated(model)
            sg.Popup("Password is empty")
            return False
        if (model.password != model.confirmPassword):
            model.passwordMismatch = True
            self.ModelUpdated(model)
            sg.Popup("Passwords do not match")
            return False
        user = datamodel.user.User(model.username, fullName=fullName)
        user.SetPassword(model.password)
        datastore.AddUser(user)
        datastore.SaveData()
        app.PopControllerFromStack()
        return True