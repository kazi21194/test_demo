from math import sqrt
import copy
class Circle:
    """Represents a circle.
       Attributes : center(point object),radius(number)
    """
    def __init__(self,centre,radius):
        self.centre = centre
        self.radius = radius

class point:
    """This represents a point
       Attributes : x,y
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y


centre = point(0,0)
cir = Circle(centre,1)

class Rectangle:
    """Represents a rectangle.
       Attributes : centre,length,breadth
    """

    def __init__(self,corner,length,breadth):
        self.corner = corner
        self.length = length
        self.breadth = breadth

pointr = point(1,0)
rect = Rectangle(pointr,1,1)

def point_in_circle(circle,point):
    """This function takes a circle and point 
       and gives true if the point lies on the circle"""
    if (point.x**2 + point.y**2 == circle.radius**2):
        return True
    else :
        return False



def rect_in_circle( circle,rect):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    
    temp = copy.copy(rect.corner)

    if(point_in_circle(cir,temp)):
        temp.x += rect.length
        if(point_in_circle(cir,temp)):    
            temp.y += rect.breadth
            if(point_in_circle(cir,temp)):    
                temp.x -= rect.length
                if(point_in_circle(cir,temp)):
                    return True
    else:
        return False

def rect_circle_overlap(circle,rect):
    """Returns true if any corner of rectangle falls inside circle"""
    temp = False
    for i in range(rect.corner.x ,(rect.corner.x + rect.length)):
        for j in range(rect.corner.y ,(rect.corner.y + rect.breadth)):
            if(point_in_circle(cir,point(i,j))):
                temp = True


    return temp

print(rect_circle_overlap(cir,rect))              
#print(point_in_circle(cir,point(75,0))) 