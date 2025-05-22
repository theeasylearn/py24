'''
write a program to findout factorial of given number 
input : 6 
process : 6 x 5 x 4 x 3 x 2 x 1 
output : 720
steps 
1   create variable number & factorial
2   accept number from user (assume number = 5)
3   store 1 in factorial 
4   factorial(5) = factorial * number 1 x 5
5   number(4) = number - 1 

6   factorial(20) = factorial(5) * number(4) 
7   number(3) = number - 1 

8   factorial(60) = factorial(20) * number(3) 
9   number(2) = number - 1 

'''
number = 0 
number = int(input("Enter number"))
factorial = 1

#condition
while number>0:
    #loop body
    factorial = factorial * number
    number = number - 1
print(factorial)

