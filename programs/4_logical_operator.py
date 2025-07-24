num1 = int(input("Enter num 1")) # 10
num2 = int(input("Enter num 2")) # 20
num3 = int(input("Enter num 3"))
#we must any one (and/or) logical operator in case of multiple relational expressions on same line 
result1 = num1 == num2 and num2 == num3
result2 = num1 == num2 or num2 == num3 

result3 = not(num1 == num2 and num2 == num3)
print(f"{result1} = {num1} == {num2} and {num2} == {num3}")
print(f"{result2} = {num1} == {num2} or {num2} == {num3}")
print(f"{result3} = not({num1} == {num2} or {num2} == {num3})")
