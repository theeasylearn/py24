# concept of inheritance (single level inheritance)
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
    
# p1 = Person()
# p1.walk()
# p1.talk()
# p1.eat()

s1 = Student()
s1.whatICanDo()