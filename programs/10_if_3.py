'''
    write a program to findout whether frame is landscape portrait or square from given dimension 
    
    steps
    1) create variable height,width
    2) accept height from user into height variable 
    3) accept width from user into width variable 
    4) check shape is portrait or not 
        if height>width == != < > <= >=
            print frame is portrait 
    5) check shape is landscape or not 
        if height<width
            print frame is landscape 
    6) check shape is square or not 
        if height==width
            print frame is square
    7) print good bye 
'''
height = None 
width = None 
height = int(input("Enter height"))
width = int(input("Enter Width"))
if height>width:
    print("frame is portrait")
if height<width:
    print("frame is landscape")
if height==width:
    print("frame is square")
print("good bye")
