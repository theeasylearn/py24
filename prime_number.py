#write a program to check whether given number is prime number or not 
'''
    1) accept number from user into number variable
    2) create divisor variable and store 2 into it 
    
    3) divide number by divisor and get reminder
    4) if reminder is zero then 
        print number is not prime number 
        stop program 
    5) increase divisor by 1
     
    6) divide number by divisor and get reminder  
    7) if reminder is zero then 
        print number is not prime number 
        stop program 
    8) increase divisor by 1
'''
def isPrime(number):
    divisor = 2
    while divisor<number:
        remainder = number % divisor
        if remainder==0:
            return False
        divisor=divisor + 1
    if number==divisor:
        return True
# number = int(input("enter number")) # 10
# result = isPrime(number)
# print(result)