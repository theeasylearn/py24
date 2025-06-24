numbers = [1,2,3,4,5,6,7,8,9,10]
number2 = [10,20,30,40,50,60,70,80,90,100]
print(numbers)
# for num in numbers:
#     print(num*num)
# map function returns map 
square_numbers = map(lambda num: num * num,numbers)
#this square_number can not be displayed directly. it has to be converted into list 
print(list(square_numbers))
sum = map(lambda a,b: a + b,numbers,number2)
sum = list(sum)
total=0
for item in list(sum):
    total+=item
print(total)