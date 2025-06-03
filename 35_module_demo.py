import asia as a 
import europe as e 
import north_america as na 
#here a, e and na are alias we can use instead of asia, europe, north_america 

print(a.getCountries())
print(e.getCountries())
print(na.getCountries())

country = input("Enter your country name")

isFound = a.hasCountry(country)
if isFound == True:
    print("you are leaving in asia")
    
isFound = e.hasCountry(country)
if isFound == True:
    print("you are leaving in europe")

isFound = na.hasCountry(country)
if isFound == True:
    print("you are leaving in north america")