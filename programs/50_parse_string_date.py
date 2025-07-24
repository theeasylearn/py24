from datetime import datetime as dt 
# this example convert string date into date object
birthdate = input("Enter your birth date (dd-mm-YYYY)")
print(birthdate)

#convert into date object
indian_format_date = dt.strptime(birthdate,'%d-%m-%Y')
print(indian_format_date) #proper date 

#show date into us format 
print(indian_format_date.strftime("%m/%d/%Y"))
print(indian_format_date.strftime("%A %b %d %Y"))
