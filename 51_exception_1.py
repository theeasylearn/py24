#make sum & average of all numbers in list
numbers = ['test',10,20,30,40,50,100,None]
sum = 0 
count = 0
for item in numbers:
    print(item)
    try:
        sum = sum + item #if error occured line no 9 will not run
        count = count + 1
    except:
        print("oops something happens, but i will manage")

average = sum/count
print(f"sum = {sum} count = {count}")
print(f"average = {average}")