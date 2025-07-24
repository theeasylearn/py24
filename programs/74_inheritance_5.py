# concept of inheritance (hierarchical inheritance)
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
class Actor(Person):
    def dance(self):
        print("I can dance")
    def fight(self):
        print("I can fight")
    def whatICanDo(self):
        super().walk()
        super().talk()
        super().eat()
        self.dance()
        self.fight()
        
s1 = Student()
s1.whatICanDo()

a1 = Actor()
a1.whatICanDo()
