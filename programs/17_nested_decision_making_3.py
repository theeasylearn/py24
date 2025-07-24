# write down a code to accept month number from user and disply name of the month.
month_number =int(input("Enter the number of the month:")) 
if month_number>=1 and month_number<=12:
    if month_number==1: 
        print("The month is january")   
    elif month_number==2:
        print("The month is february")
    elif month_number==3:
        print("The month is march")
    elif month_number==4:
        print("This month is april")
    elif month_number==5:
        print("This month is may")
    elif month_number==6:
        print("This month is jun")
    elif month_number==7:
        print("This month is july")
    elif month_number==8:
        print("This month is august")
    elif month_number==9:
        print("This month is september")
    elif month_number==10:
        print("This month is october")
    elif month_number==11:
        print("This month is november")
    elif month_number==12:
        print("This month is december")
else:
    print("invalid month number")