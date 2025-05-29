#default argument function 
def getSquare(x,y=2):
    # print(x)
    # print(y)
    result = (x * x) + (2 * x * y) + (y * y) 
    return result

result = getSquare(10,5)
print(result)
result = getSquare(5)
print(result)