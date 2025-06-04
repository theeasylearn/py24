import math 
import sys 
import datetime

#get all function and constant in math module
def showFunctions(module):
    list = dir(module)
    print(f"functions in {module} module")
    for item in list:
        print(item)
    
showFunctions(math)
showFunctions(sys)
showFunctions(datetime)