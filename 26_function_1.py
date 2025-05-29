# write a program to implement Pythagoras Theorem:

#create user defined function 

#with return value with argument(input)
def getSquare(number):
    #create local variable
    square = number * number
    return square
# Without return value without argument
def printLine():
    print("*" * 125)
    return None 

printLine() #calling function printline
a = int(input("Enter value for A"))
a_square = getSquare(a) #calling function
b = int(input("Enter value for B"))
b_square = getSquare(b) #calling function

c_square = a_square + b_square
printLine()
print(c_square)
printLine()
