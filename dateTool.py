import datetime
from datetime import datetime

def DateTimeToString(dateTime):
    if dateTime == None:
        return None
    return dateTime.strftime("%Y-%m-%d %H:%M:%S")
def StringToDateTime(string):
    if string == None:
        return None
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")