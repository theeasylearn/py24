#create class 
class Person:
    #function are called methods 
    def walk(self):
        print("Person can walk")
    def talk(self):
        print("Person can talk")
    def sleep(self):
        print("Person can sleep")
        
#create object
ankit = Person() #calling function, we never supply value for self in any function
harsh = Person()
nihar = Person()

ankit.walk()
harsh.talk()
nihar.sleep()
