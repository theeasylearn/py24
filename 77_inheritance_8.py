#2nd example of multiple inheritance
class Square:
    def __init__(self,size):
        self.size = size 
    def getArea(self):
        area = self.size * self.size
        return area
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width 
    def getArea(self):
        area = self.length * self.width 
        return area 
class MarriageHall(Square,Rectangle):
    def __init__(self,size,length,width):
        Square.__init__(self,size)
        Rectangle.__init__(self,length,width)
    def getArea(self):
        area = Square.getArea(self) + Rectangle.getArea(self)
        return area    
    
size = 100
length = 10 
width = 20
m1 = MarriageHall(size,length,width)
area = m1.getArea()
print(f"area of marriage hall = {area}")
