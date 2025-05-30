def getMeritTotal(maths,science,english,hindi,gujarati,computer):
    total = maths + science + english
    return total 


maths = 80
science = 90 
english = 95 
hindi = 41
gujarati = 51
computer = 35 
 
# total = getMeritTotal(maths,science,hindi,gujarati,computer,english) not good way to call function

#keyword arguments
total = getMeritTotal(maths=80,hindi=41,gujarati=51,science=90,english=95,computer=35) 
print(total)

total = getMeritTotal(gujarati=gujarati,science=science,english=english,computer=computer,maths=maths,hindi=hindi)

print(total)
