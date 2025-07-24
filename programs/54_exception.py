#example try except block without exception type 
result = 0
try:
    num1 = int(input("enter num1 "))
    num2 = int(input("enter num2 "))
    result = num1 / num3 
except: 
    print("oops something went wrong. please try again")
else:
    print(f'Program finished successfully {result}')
    