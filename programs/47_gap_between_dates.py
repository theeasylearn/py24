from datetime import datetime 
import math
def getDate(msg):
    print(msg)
    day = int(input("Enter day"))
    month = int(input("Enter month"))
    year = int(input("Enter year"))
    mydate = datetime(year,month,day)
    return mydate

person1 = getDate("Enter first person birthdate")
person2 = getDate("Enter second person birthdate")

timestamp1 = person1.timestamp()
timestamp2 = person2.timestamp()

print(timestamp1,timestamp2)

difference = math.fabs(timestamp1 - timestamp2)
print("difference in seconds",difference)

days = difference / (60 * 60 * 24)
years = days / 365
print(f"days = {days} years = {years}")
