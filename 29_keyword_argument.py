def getMeritTotal(maths,science,english,hindi,gujarati,computer):
    total = maths + science + english
    return total 


maths = 80
science = 90 
english = 95 
hindi = 41
gujarati = 51
computer = 35 
 
total = getMeritTotal(maths,science,hindi,gujarati,computer,english)
print(total)