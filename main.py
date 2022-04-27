import data
import app

datastore = data.GetDataStore()

app.PrepareLogin()

while app.HasControllerOnStack():
    controller, model = app.PopControllerFromStack()
    controller.Show(model)