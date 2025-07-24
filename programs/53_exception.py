# example of simple user defined exception 
# write a program to accept amount user want's to withdraw from his bank account. if remaining amount is less then 5000 Rs then do not allowed user to withdraw money. allow user to do 3 attempt 
balance = 50000
count = 1
while True and count<4:
    try:
        amount = int(input("Enter withdrawal amount ")) # 46000
        temp = balance - amount # 50000 - 46000
        if temp<5000:
            # raise keyword is used to raise run time error
            raise ValueError
        else:
            balance = temp 
    except ValueError:
        print('you must have 5000 Rs balance in your account after withdrawal, please try again')    
        count=count + 1
    else:
        #else block in this case will run only if except block do not run
        print(f'remaining balance in your account = {balance}')
        break


