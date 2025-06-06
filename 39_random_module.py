import random as rd 
#here rd as alias for random 

#generate random number between 0.0 and 1.0 
print(rd.random())

#generate float random number between 10 to 99
print(rd.uniform(10,99))

#generate integer random number between 10 to 99
print(rd.randint(10,99))

#generate integer random number between 10 to 100 divisible by 10
print(rd.randrange(10,99,10))
