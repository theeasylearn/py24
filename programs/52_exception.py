#write a program to findout qube of given positive number with exception handling mechanism 
import math
try:
    number = int(input("Enter positive number to findout qube")) #this line can generate exception (run time error due to invalid input)
    if number<0:
        print('it is negative number, so let us convert it into positive number')
    number = math.fabs(number)
    qube = number * number * number 
    print(f"qube = {qube}")

except ValueError:
    #except block will run only in case of ValueError exception
    print("it is not valid input")
