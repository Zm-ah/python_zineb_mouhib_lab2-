from shape import Shape
from numbers import Number

class Rectangle(Shape):
    def __init__(self, x= 0 ,y= 0 , width = 2 ,heigth = 2):
        super().__init__(x, y)
        
        if not isinstance( width , Number) or not isinstance(heigth , Number):
            raise TypeError(" ---- The parameter must be positiv!---- ")
        if width <= 0 or heigth <= 0:            
            raise ValueError(" ---- The width and the heigth must be positive ----")
        self._width = width 
        self._heigth =  heigth     


    @property
    def width(self):
        return self._width 
    @property
    def heigth(self):
        return self._heigth 
    # dubbel kolla med att làgga privat underskor med làraren imorgon 
    @property 
    def area(self):
        return self._width * self._heigth 
    @property 
    def perimeter(self):
        return 2 * (self._width + self._heigth)
    @property
    def center(self):
        return(self._x + self._width/2, self._y + self._heigth/2)
    


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
    


    def __str__(self):
        return f"rectangle {self._x},{self._y},{self._width},{self.heigth})"
   
    def __repr__(self):
        return f"rectangle (width ={self._width},heigth = {self.heigth}, area ={self.area:2f}., perimeter= {self.perimeter:2f}))"