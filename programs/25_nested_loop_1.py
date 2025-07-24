'''
write a program to print following pattern (only one astrik at time will be displayed)

*
* *
* * *
* * * *
* * * * *
'''
row = 1
while row<=5: #outer loop
    column=1
    while column<=row: #inner loop 
        print('*',end=' ')
        column=column+1
    print(" ") #new line 
    row=row+1

