# concept of inheritance (multi-level inheritance)
class Person: #Parent/root/base class
    #methods
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")
#inheritance
class Student(Person): #Child/sub/Derived class 
    #methods 
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def whatICanDo(self):
        #calling parent class method
        super().walk()
        super().talk()
        super().eat()
        #calling own class method
        self.read()
        self.write()    

#leaf class (last inherited class)
class PythonDeveloper(Student):
    def code(self):
        print("I can write code in python")
    def debug(self):
        print("I can debug code in python")
    #Method Overidding
    def whatICanDo(self):
        super().whatICanDo()
        self.code()
        self.debug()
        
#create leaf class object
p1 = PythonDeveloper()
p1.whatICanDo()