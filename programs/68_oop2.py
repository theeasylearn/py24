class Student:
    #constructor function
    #now add parameters 
    def __init__(self,name,english,maths,science):
        print('constructor function called...')
        #create instance variable 
        self.name = name
        self.english = english
        self.maths = maths
        self.science = science
        self.total = self.english + self.maths + self.science
        self.average = self.total / 3
    def display(self):
        print(self.name)
        print(self.maths)
        print(self.english)
        print(self.science)
        print(self.total)
        print(self.average)
        
#create object 
s1 = Student('Saloni Vasoya',70,80,85) #it will call constructor means __int__ method
s1.display()   

s2 = Student('Shital Dobriya',80,90,100)
s2.display()


