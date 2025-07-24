'''
    write a program to findout largest number from 3 given number
    
    num1 = 10
    num2 = 11
    num3 = 09
    
    num1 = 12
    num2 = 11
    num3 = 09
    
    num1 = 12
    num2 = 11
    num3 = 13
    
    steps
    --------------
    1) create variable num1,num2,num3 
    2) accept input from user in variable num1
    3) accept input from user in variable num2
    4) accept input from user in variable num3
    5) compare num1 and num2 to findout largest number 
        if num1>num2: # == <= >= < > !=
    6)      if num1>num3: # == <= >= < > !=
    7)          print("num1 is largest number")
    8)      else:
    9)          print("num3 is largest number")
    10) else
    11)     if num2>num3:
    12)         print("num2 is largest number")
    13)     else
    14)         print("num3 is largest number")
'''
num1 = num2 = num3 = 0 #chain assignment 
num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))
num3 = int(input("Enter num 3"))
if num1>num2:
    if num1>num3:
        print("num1 is largest number")
    else:
        print("num3 is largest number")
else:
    if num2>num3:
        print("num2 is largest number")
    else:
        print("num3 is largest number")
        
print("Good bye")