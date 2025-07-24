# write a program to read numbers from file and store it in odd.txt file if number is odd otherwise store it into even.txt file 
try:
    read_file = open('numbers11.txt','r')
    odd_file = open('odd.txt','w')
    even_file = open('even.txt','w')
    for line in read_file:
        try:
            number = int(line)
            if number==0:
                print('it is nither odd nor even so number is skipped')
            else:
                remainder = number % 2
                if remainder==0: #even
                    even_file.write(str(number) + '\n')
                else:
                    odd_file.write(str(number) + '\n')
                print(number)
            read_file.close()
            odd_file.close()
            even_file.close()
        except ValueError:
            print(f'{line} is not number so it is skipped')
except FileNotFoundError:
    print('file you are trying to access does not exists')