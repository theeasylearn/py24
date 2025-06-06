import random as rd 
lucky_number  = rd.randint(1,100)
start = 1
stop = 100
guess_number = int(input(f"Enter your guess between {start} to {stop}"))
if lucky_number == guess_number:
    print("Congratulation you have win 10000 Rs")
    
if lucky_number<guess_number:
    start = 1
    stop = lucky_number
else: 
    start = lucky_number
    

guess_number = int(input(f"Enter your guess between {start} to {stop}"))
if lucky_number == guess_number:
    print("Congratulation you have win 1000 Rs")
    
if lucky_number<guess_number:
    start = 1
    stop = lucky_number
else: 
    start = lucky_number
    
guess_number = int(input(f"Enter your guess between {start} to {stop}"))
if lucky_number == guess_number:
    print("Congratulation you have win 100 Rs")
    
if lucky_number<guess_number:
    start = 1
    stop = lucky_number
else: 
    start = lucky_number
    
