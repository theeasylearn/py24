# write a program to read numbers from file and store it in odd.txt file if number is odd otherwise store it into even.txt file 

read_file = open('numbers.txt','r')
odd_file = open('odd.txt','w')
even_file = open('even.txt','w')

for line in read_file:
    number = int(line)
    remainder = number % 2
    if remainder==0: #even
        even_file.write(str(number) + '\n')
    else:
        odd_file.write(str(number) + '\n')
    print(number)
read_file.close()
odd_file.close()
even_file.close()
