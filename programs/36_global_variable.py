amount = 100 
def addMoney(rs):
    # in below 2 line python assume you want to update local variable amount
    # amount = 0
    # amount = amount + rs 
    
    # in below 2 line python assume you want to update global variable amount 
    global amount 
    amount = amount + rs
    print('addMoney method is called...')

print(f"before addMoney method called amount = {amount}")
rs = int(input("Enter how much rs you want to add in your account"))
addMoney(rs)
print(f"after addMoney method called amount = {amount}")
