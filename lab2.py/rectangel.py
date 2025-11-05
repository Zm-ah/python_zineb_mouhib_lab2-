from shape import Shape
class rectangle(Shape):
    def __init__(self,width, heigth, x, y ):
        super().__init__(x ,y )
        if width <= 0 or heigth <= 0:            
            raise ValueError(" the width and the heigth most be positive")
        self.width = width 
        self.heigth =  heigth     

    # dubbel kolla med att làgga privat underskor med làraren imorgon 
    @property 
    def area(self):
        return self.width * self.height 

    @property 
    def perimeter(self):
        return 2 * (self.width + self.height)
