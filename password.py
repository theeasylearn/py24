#this is local module 
import string
import random as rd 
def generatePassword(size=12):
    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    # print(all_chars)
    #convert string all_chars into list. list should have one letter at each position
    seeds = list(all_chars)
    start = 0 
    stop = len(seeds) - 1
    rd.shuffle(seeds)
    
    password = [] #empty list
    for count in range(1,size+1):
        password.append(seeds[rd.randint(start,stop)])
    
    return ''.join(password)
#call function
random_password = generatePassword()
print(random_password)

random_password = generatePassword(size=32)
print(random_password)