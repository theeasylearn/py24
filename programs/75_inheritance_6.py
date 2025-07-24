#hierarchical level inheritance
# parent class
class myMath:
    def getSquare(self,number):
        #create local variable
        square = number * number
        return square
    def getPi(self):
        return 3.1415
#child class
class Circle(myMath):
    #constructor
    def __init__(self,radius):
        #calling parent constructor
        super().__init__()
        #create instance variable 
        self.radius = radius
        print('Circle class constructor called...')
    def getArea(self):
        #calculate and return area of Circle
        #pi * radius * radius
        area = super().getPi() * super().getSquare(self.radius)
        return area

class Square(myMath):
    def __init__(self,size):
        super().__init__()
        self.size = size 
    def getArea(self):
        area = super().getSquare(self.size)
        return area 
    
#create object

radius = int(input("Enter radius of circle"))
c1 = Circle(radius)
area = c1.getArea()
print(f"area of circle = {area}")

size = int(input("Enter size of square"))
s1 = Square(size)
area = s1.getArea()
print(f"area of square = {area}")