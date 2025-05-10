# example of arithmetic operator
# write a program to do addition subtraction multiplication division floor division and power on given two number 
num1 = input("Enter num 1")
num2 = input("Enter num 2")

#convert input (num1,num2) into integer 
num1 = int(num1)
num2 = int(num2)

#process (expression/samikaran)
#binary operator
# variable-name operator variable-name
addition = num1 + num2
subtraction = num1 - num2 
multiplication = num1 * num2 
division = num1 / num2 
reminder = num1 % num2 
power = num1 ** num2 # 5 ^ 3 = 5 * 5 *5 = 125
floor_division = num1 // num2 

#display 
print("addition = " + str(addition))
print("subtraction = " + str(subtraction))
print("multiplication = " + str(multiplication))
print("division = " + str(division))
print("reminder = " + str(reminder))
print("power = " + str(power))
print("floor_division = " + str(floor_division))
