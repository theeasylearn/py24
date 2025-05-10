fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Strawberry", "Watermelon", "Papaya", "Kiwi"]

fav_fruit = input("Enter your favorite fruit name")

is_found = fav_fruit in fruits
print(is_found)

vegetables = ("Potato", "Onion", "Tomato", "Brinjal", "Ladyfinger", "Bottle Gourd", "Bitter Gourd", "Drumstick", "Cabbage", "Cauliflower")

fav_vegis = input("Enter your favorite vegetable name")
is_found = fav_vegis not in vegetables
print(is_found)

indian_states = "Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil Nadu, Telangana, Tripura, Uttar Pradesh, Uttarakhand, West Bengal"

state = input('where are you from? (state)')

is_found = state in indian_states
print(is_found)