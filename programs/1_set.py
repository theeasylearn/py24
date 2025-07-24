#concept of set 
fruits = {'apple','banana','mango'}
print(fruits)

#add new item 
fruits.add('orange')
fruits.add('apple') #it will be ignore 
fruits.add('kiwi')
print(fruits)

#remove item 
fruits.remove('kiwi')
# fruits.remove('coconut') #will generate error when we try to remove non existing item
print(fruits)