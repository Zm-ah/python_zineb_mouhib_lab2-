from numbers import Number


class Shape:  # creating a class shape, the blue print for the othar classes
    def __init__(self, x=0, y=0):
        if not isinstance(x, Number) or not isinstance(y, Number): # the parameter have to be numbers, and then I'm raisen an error value to evoid typing erro in case we write a string or a boolean. 
            raise TypeError("x and y must be numeric values")
         
        # save the atribute value internally in the objects 
        self._x = x 
        self._y = y  
    
    # getter
    @property
    def x(self):
        return self._x # function that give the value of _x 

    @property
    def y(self):
        return self._y # function that give the value of _y 

    def translate(self, dx, dy): # This giv oss the posibility to move the shapes on x and y 
        if isinstance( dx, bool) or isinstance(dy, bool ): # som validations for eventual error 
            raise TypeError(" ---- The value cannot be a boolean ---- ")
        if not isinstance( dx ,Number ) or not isinstance(dy,Number):
            raise TypeError(" ---- The value must be a number ---- ")
        self._x += dx
        self._y += dy

    # creating functions with som comparison operator for the X and Y 

    def __eq__(self, other):  # equale to  c.o
        return (self.x == other.x) and (self.y == other .y)

    def __le__(self, other):  # less than or equale to  c.o
        return (self.x <= other.x) and (self.y <= other.y)

    def __ge__(self, other):  # greater than or equale to c.o
        return (self.x >= other.x) and (self.y >= other.y)

    def __lt__(self, other):  # less than c.o
        return (self.x < other.x) and (self.y < other.y)

    def __gt__(self, other):  # great than c.o
        return (self.x > other.x) and (self.y > other.y)