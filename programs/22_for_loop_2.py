# write a program to count vowels in given string 
# a e i o u 
name = input("Enter your name")
count = 0
print(name)
for letter in name:
    # print(letter)
    letter = letter.lower()
    if letter == 'a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        count += 1
print(f"no of vowels = {count}")