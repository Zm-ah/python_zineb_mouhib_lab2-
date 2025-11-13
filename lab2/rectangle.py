from shape import Shape
from numbers import Number

class Rectangle(Shape): # creating class R. with inherits from shape. 
    def __init__(self, x= 0 ,y= 0 , width = 2 ,height = 2): # the constructure 
        super().__init__(x, y) #  calling the constructure from the shape class. 
        
        if not isinstance( width , Number) or not isinstance(height , Number):  # validating parameters and make sure they are Numbers. 
            raise TypeError(" ---- You must type a number ---- ")
        if width <= 0 or height <= 0:            
            raise ValueError(" ---- The width and the heigth must be positive ----")
        self._width = width   # save the atribute value internally in the objects  
        self._height =  height    

              
    @property  # som property functions 
    def width(self):
        return self._width 
    @property
    def height(self):
        return self._height 
    
    @property 
    def area(self):
        return self._width * self._height
    @property 
    def perimeter(self):
        return 2 * (self._width + self._height)
    @property
    def center(self):
        return(self._x + self._width/2, self._y + self._height/2)
    


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
    


    def __repr__(self): # return string representation of the Rectangle objekt. 
        return f"Rectangle (x = {self._x}, y = {self._y},width = {self.width}, height = {self.height})"
   
    def __str__(self): # return the area and perimeter of the rectangle 
        return f"Rectangle ( center= ({self._x},{self._y}), area ={self.area:.2f}., perimeter= {self.perimeter:.2f} )"