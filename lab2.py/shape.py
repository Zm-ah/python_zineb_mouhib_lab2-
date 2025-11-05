import numbers
from numbers import Number
class Shape:  # creating a class shape, the blue print for the othar classes 


    def __init__(self,  x = 0 , y = 0  ):
        if not isinstance(x,(numbers.Number)) or not not isinstance(y,(numbers.Number)):
            raise TypeError("x and y must be numeric values")
        
        self._x = x  # the coordinate of the center 
        self._y = y # the second cordinate of the center 
         
    
    # getter 
    @property 
    def x(self):
        return self._x
        
    @property 
    def y(self):
        return self._y 
    
    
    # read-only 
    @property 
    def area (self):
       return self._area 

    @property 
    def parimeter(self):
        return self._perimeter
    
    def translate( self, dx , dy ):
        self._x += dx
        self._y += dy 


  # creating functions with som comparison operator 

    def __eq__(self, other): # equale to  c.o 
        return self.area == other. area
    
    def __le__(self,other): # less than or equale to  c.o 
        return self.area <= other.area
    
    def __ge__(self, other): # greater than or equale to c.o
        return self.area >= other.area

    def __lt__(self, other): # less than c.o 
        return self.area < other.area 
    
    def __gt__(self, other): #great than c.o 
        return self.area > other.area 
    
    

