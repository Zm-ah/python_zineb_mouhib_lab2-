from shape import Shape 
import math
class Circle(Shape):
    def __init__(self, x = 0, y = 0 , radius = 3):
        
        super().__init__(x, y)
        self.radius = radius 

        if radius <= 0:
            raise ValueError("Radius most be posotive")
            self.radius = radius 

    @property 
    def area(self):
        return math.pi * self.radius**2 
        
    @property 
    def perimeter(self):
            return 2 * math.pi * self.radius 