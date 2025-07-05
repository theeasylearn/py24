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

class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)
    def getSurfaceArea(self):
        surfaceArea = 4 * super().getArea()
        return surfaceArea
    
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
# c1.radius = 0
# print(f"radius = ",c1.radius)
print(f"area of circle = {area}")

sp1 = Sphere(radius)
surfaceArea = sp1.getSurfaceArea()
print(f"surfaceArea of sphere is = {surfaceArea}")

size = int(input("Enter size of square"))
s1 = Square(size)
area = s1.getArea()
print(f"area of square = {area}")