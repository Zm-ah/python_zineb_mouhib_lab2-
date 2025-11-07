from shape import Shape
from numbers import Number 
import math

class Circle(Shape): # creating class Circle with inherits from shape
    def __init__(self, x=0, y=0, radius=3):# the cunstructure for the circle 
        super().__init__(x, y) # calling for the constructions from shape class 
        if isinstance(radius, bool): # validating 
            raise TypeError (" The radius cannot be boolien")
        if not isinstance(radius, Number):
            raise TypeError( "You must type numbers")
        if radius <= 0:
            raise ValueError("Radius must be posotive")
        
        self._radius = radius  # save the value in the objekt 

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def radius(self):
        return self._radius

    @radius.setter  
    def radius(self, value): # function that take value and validating it 
        if isinstance ( value, bool): # validating for bolien  
            raise TypeError(" The radius must be a number")
        if not isinstance(value, Number): # validating for numeric value 
            raise TypeError( "you must type numbers")
        elif value <= 0: # vaidating for a positiv number 
            raise ValueError(" Radius must be positive")
        
        self._radius = value # save the value in the objekt 

    def unit_circle(self)->bool: # function that givs a bool when the circle is unit circle. 
        return self._x == 0 and self._y == 0 and self.radius == 1 
    
    @property
    def center(self):
        return(self._x , self._y) # function tha givs the center of   


     # creating functions with som comparison operator
   
    def __eq__(self, other):  # equale to  c.o
        return self.area == other.area

    def __le__(self, other):  # less than or equale to  c.o
        return self.area <= other.area

    def __ge__(self, other):  # greater than or equale to c.o
        return self.area >= other.area

    def __lt__(self, other):  # less than c.o
        return self.area < other.area

    def __gt__(self, other):  # great than c.o
        return self.area > other.area
    

    def __repr__(self):# return string representation of the Circle objekt. 
        return f"Circle(x = {self.x}, y = {self.y} , radius={self._radius})"

    def __str__(self):# return the area and perimeter of the circle   
        return f"Circle(center= ({self._x},{self._y}), radius = {self.radius} , area = {self.area:.2f}, perimeter = {self.perimeter:.2f})"
