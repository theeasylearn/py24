from datetime import datetime,time
def getTime(msg):
    hours = int(input("Enter hours"))
    minutes = int(input("Enter minutes"))
    seconds = int(input("Enter seconds"))
    mytime = time(hours,minutes,seconds)
    return mytime

entry_time = getTime("Enter entry time")
exit_time = getTime("Enter exit time")
print(entry_time)
print(exit_time)
difference =  datetime.combine(datetime.today(), exit_time) - datetime.combine(datetime.today(),entry_time)

print(difference)
