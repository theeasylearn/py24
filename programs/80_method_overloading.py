class AreaCalculator:
    def getArea(self,length=None,width=None):
        if length is not None and width is not None:
            return length * width
        elif length is not None:
            return length * length
        else:
            return 0 

#create object 
area = AreaCalculator()
print(area.getArea()) # 0
print(area.getArea(10)) # 100
print(area.getArea(10,20)) # 200