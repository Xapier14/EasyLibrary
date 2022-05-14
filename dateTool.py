import datetime
from datetime import date
from datetime import datetime
def GetToday():
    return datetime.now()
def GetDaysBetween(dateTime1, dateTime2):
    return (dateTime2.date() - dateTime1.date()).days
def DateTimeToString(dateTime):
    if dateTime == None:
        return None
    return dateTime.strftime("%Y-%m-%d %H:%M:%S")
def StringToDateTime(string):
    if string == None:
        return None
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")