# concept of lambda function 
getSquare = lambda num : num * num 
getQube = lambda number : number * number * number
getNSquare = lambda x,y : getSquare(x) + 2 * x * y + getSquare(y) 

number1 = int(input("enter number"))
result = getSquare(10)
print (f"square of {number1} {result}")
result = getQube(number1)
print (f"qube of {number1} {result}")
result = getNSquare(3,5)
print (f"nsquare of x = 3 and y = 5 {result}")

 