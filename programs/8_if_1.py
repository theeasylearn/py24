# write a program to find out qube of given positive number 
'''
    steps 
    ---------------------------
    1  create variable number and qube 
    2  accept input from user into number variable 
    3  if number is negative then  
        3.1 convert negative number into positive number 
        3.2 print message number is converted into positive number 
    4   calculate qube of number and store it into qube 
    5   display qube variable
'''
number = 1
qube = 1 
number = int(input("Enter positive number to get qube")) # -10
if number<0: # < > <= >= == != 
    number = 0 - number 
    print('number was negative number so it is converted into positive number')
qube = number * number * number
print(qube)