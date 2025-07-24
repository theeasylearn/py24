'''
    write a program to display 24 hours format time given by user into 12 hours format time 
    steps 
    --------------------------------------------------
    1) create variable hours 
    2) accept input from user in hours variable 
    3) check hours are within range of 0 to 24 
        if hours>=0 and hours<=24 then 
            4) check hours > 12 then 
                hours = hours - 12 
                print hours with pm sign 
            5) else 
                print hours with am sign 
      otherwise 
        print("invalid hours")

'''
hours = int(input("enter hours in 12 hours format"))
if hours>=0 and hours<=24: #outer decision making statement
    if hours>12: #inner decision making statement
        hours = hours - 12 
        print(f"{hours} PM")
    else:
        print(f"{hours} AM")
else:
   print("invalid hours")
    