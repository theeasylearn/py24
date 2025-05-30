# function that returns multiple values 
def getResult(num1,num2):
    #create local variables 
    addition = num1 + num2 
    subtraction = num1 - num2 
    multiplication = num1 * num2 
    division = num1 / num2 
    return addition,subtraction,multiplication,division

num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

#multiple value are returned from function as tuple
result = getResult(num1,num2)
print(result)