import random as rd 

lucky_number  = rd.randint(1,100)
start = 1
stop = 100
prize = 10000
attempt = 1
while attempt<=3:
    guess_number = int(input(f"Enter your guess between {start} to {stop}"))
    if lucky_number == guess_number:
        print(f"Congratulation you have win {prize} Rs")
        break #stop loop 
    elif lucky_number<50:
        start = 1
        stop = stop // 2
    else: 
        start = 50
    prize = prize // 10 
    attempt=attempt+1

if attempt==4:
    print("better luck next time....")
    print(f"lucky number was {lucky_number}")