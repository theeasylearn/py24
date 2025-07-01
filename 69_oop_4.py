#concept of class variable 
class Society:
    Hall = "People Welfare Community hall"
    Gate1 = False #False means gate is closed
    Gate2 = True #True means gate is open 
    #constructor
    def __init__(self,tower,floor,flatno,owner):
        self.tower = tower
        self.floor = floor 
        self.flatno = flatno 
        self.owner = owner
        print('constructor is called...')
    #methods
    def display(self):
        print(f"tower = {self.tower} floor = {self.floor} flatno = {self.flatno} owner = {self.owner}")

#create object
# object_name = ClassName()

s1 = Society('gulab',1,101,'Ram kumar')
s2 = Society('Dollar',2,205,'Krishna ben sharma')
print("accessing class variable(shared variables)")
print(Society.Hall)
print(Society.Gate1)
print(Society.Gate2)
#updating class variable
Society.Gate1 = True 
Society.Gate2 = False 
print(Society.Gate1)
print(Society.Gate2)
s1.display()
s2.display()
