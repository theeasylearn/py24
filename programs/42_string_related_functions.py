#string related functions
name = "   The EasyLearn Academy  "
print(name.upper())  # Convert to uppercase
print(name.lower())  # Convert to lowercase
print(name.title())  # Convert to title case
print(name.capitalize())  # Convert to capitalized case
print(name.swapcase())  # Swap case
print(name.startswith("The"))  # Check if string starts with "The"
print(name.endswith("Academy"))  # Check if string ends with "Academy"
print(name.find("Easy"))  # Find the index of substring "Easy"
print(name.replace("Easy", "Simple"))  # Replace "Easy" with "Simple"
print(name.split())  # Split the string into a list of words
print(name.split(" "))  # Split the string by space
print(len(name))  # Get the length of the string
print(name.count("a"))  # Count occurrences of "a"
print(name.isalpha())  # Check if all characters are alphabetic 
print(name.isalnum())  # Check if all characters are alphanumeric
print(name.isdigit())  # Check if all characters are digits
print(name.islower())  # Check if all characters are lowercase
print(name.isupper())  # Check if all characters are uppercase
print(name.strip())  # Remove leading and trailing whitespace
print(name.lstrip())  # Remove leading whitespace   
print(name.rstrip())  # Remove trailing whitespace
print(name.center(50, '*'))  # Center the string with '*' padding