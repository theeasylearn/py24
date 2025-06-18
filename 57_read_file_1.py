#write a program to read file 
filename = 'country.txt'
mode = 'r' #r = read mode (only file read operation is possible)
#open file 
file = open(filename,mode)

#fetch each line and display it 
count = 0
for line in file:
    print(line,end='')
    count=count+1
print()
print(f"count = {count}")