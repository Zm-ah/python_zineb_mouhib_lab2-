from shape import Shape
import math


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=3):
        super().__init__(x, y)
        if radius <= 0:
            raise ValueError("Radius must be posotive")
        self._radius = radius

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
    def radius(self, value):
        if value <= 0:
            raise ValueError(" Radius must be positive")
        self._radius = value


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
    

    def __repr__(self):
        return f"Circle(radius={self._radius}),center= ({self._x},{self._y})"

    def __str__(self):
        return f"Circle(center= ({self._x},{self._y}), radius  ={self.radius} , area ={self.area:2f}, perimeter {self.perimeter:2f})"
