#write a program to find out given number is odd or not (display message number is odd otherwise do not display message)
'''
    steps 
    ---------------
    1   create variable number 
    2   accept input from user into number 
    3   get reminder of number/2 and store in reminder variable
    4   if number is odd then 
        4.1 print message given number is odd number 
    5   print good bye  
'''
number = None 
number = int(input('enter number'))
reminder = number%2
if reminder==1: # < > <= >= == !=
    print('given number is odd number')
print('good bye')