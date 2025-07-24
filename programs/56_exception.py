from datetime import datetime
user_given_date = input("enter your birth date dd-mm-YYYY")
#convert it into date object
try:
    birth_date = datetime.strptime(user_given_date,"%d-%m-%Y")
except ValueError:
    print("you have given invalid date")
else:
    print("formatted date is ",birth_date.strftime("%A %d %B %Y"))
finally:
    print("good bye....")