#example try except block without exception type 
result = 0
while True:
    try:
        num1 = int(input("enter num1 "))
        num2 = int(input("enter num2 "))
        result = num1 / num2 
    except ValueError: 
        print("invalid input, only numbers are allowed")
    except ZeroDivisionError:
        print("zero division error, try again ")
    except Exception as e:
        print(e)
        print('other error occurred')
    else:
        print(f'Program finished successfully {result}')
        break
print('program finished.....')