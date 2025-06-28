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
name = input("enter student name")
english = int(input("enter english mark"))
maths = int(input("enter maths mark"))
science = int(input("enter science mark"))

s1 = Student(name,english,maths,science) #it will call constructor means __int__ method
s1.display()   

name = input("enter student name")
english = int(input("enter english mark"))
maths = int(input("enter maths mark"))
science = int(input("enter science mark"))

s2 = Student(name,english,maths,science)
s2.display()


