'''
    write a program to display 24 hours format time given by user into 12 hours format time 
    steps 
    --------------------------------------------------
    1) create variable hours 
    2) accept input from user in hours variable 
    3) check hours > 12 then 
        hours = hours - 12 
        print hours with pm sign 
    4) else 
        print hours with am sign 

'''
hours = int(input("enter hours in 12 hours format"))
if hours>12:
    hours = hours - 12 
    print(f"{hours} PM")
else:
    print(f"{hours} AM")
