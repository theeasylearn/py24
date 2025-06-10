from datetime import date 
def getDate(msg):
    print(msg)
    day = int(input("Enter day"))
    month = int(input("Enter month"))
    year = int(input("Enter year"))
    mydate = date(year,month,day)
    return mydate

due_date = getDate("Enter due date")
payment_date = getDate("Enter payment date")
print(due_date)
print(payment_date)

if due_date>payment_date:
    print("payment before due date so there will be no penalty")
else:
    print("payment after due date so there will be 1000 penalty")

