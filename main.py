# EasyLibrary
# Lance Crisang - 2022

# https://www.github.com/xapier14/EasyLibrary

import ctypes
import platform
import data
import app
import make

# dpi awareness flag for windows
# if platform.system() == "Windows":
#     if platform.release() == "7":
#         ctypes.windll.user32.SetProcessDPIAware()
#     elif platform.release() == "8" or platform.release() == "10":
#         ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Prepare datastore
datastore = data.GetDataStore()

# Prepare initial login controller
app.PushPairToStack(make.MakeLogin(datastore))

# Main program loop
while app.HasControllerOnStack():
    controller, model = app.PeekControllerFromStack()
    controller.Show(model)