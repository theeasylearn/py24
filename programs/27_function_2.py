# With return value Without argument
from datetime import datetime 
from playsound3 import playsound

def getDateTime():
    now = datetime.now()
    return now 

def getDate():
    now = datetime.now()
    # 29-05-2025 
    today = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
    return today

def getTime():
    now = datetime.now()
    # 17:56 
    time = str(now.hour) + ":" + str(now.minute)
    return time 

def ringBell():
    playsound("bell.mp3")
    
#without return value With argument 
#call function 
result = getDateTime()
print(result)

print(getDate())
print(getTime())
ringBell()
