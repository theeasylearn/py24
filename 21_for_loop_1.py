fruits = ["Mango", "Banana", "Guava", "Papaya", "Pomegranate", "Jackfruit", "Lychee", "Custard Apple", "Indian Gooseberry", "Sapota"]

print(fruits)

#display one fruit in one line 
#count items 
count=0
for item in fruits:
    print(item)
    count=count+1
print(count)

vegetables = ("Potato", "Tomato", "Onion", "Brinjal", "Okra", "Bitter Gourd", "Bottle Gourd", "Spinach", "Cabbage", "Cauliflower")
print("*"*100)
#print each and every vegetables in lower case 
for element in vegetables:
    print(element.lower())
    
print("*"*100)
#Dictionary
marks = {"Math": 88, "English": 75, "Science": 92, "History": 80, "Geography": 78, "Computer": 95}

#calculate total & Average
total = 0
count = 0
for subject in marks:
    print(subject + str(marks[subject]))
    total += marks[subject]
    count += 1

average = total / count
print(f"total = {total} average = {average}")    


