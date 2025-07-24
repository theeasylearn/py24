# concept of is and is not operator 
x = 10 
y = 20 
#here x and y has different value so there address will be different 
result = x is y 
address_of_x = id(x) #id function returns address of the variable in main memory
address_of_y = id(y)
print(result,address_of_x,address_of_y)

#let us create two other variable 
a = 100
b = 100
#here a and b has same value therefore there will will be same 
result = a is b 

address_of_a = id(a)
address_of_b = id(b)
print(result,address_of_a,address_of_b)