#print 1 to 10 using for loop 
for number in range(1,11):
    print(number)
    
    
#count odd number between 1 t0 10
count = 0
for number in range(1,11):
    if number%2==1:
        count+=1
print(f"odd number between 1 to 10 {count}")