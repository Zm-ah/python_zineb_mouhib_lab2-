class Shapes:  # creating a class with a center(x,y) and radius from the center to the parameter. 
    def __init__(self,  x = 0 , y = 0  ):
        self.x = x  # the coordinate of the center 
        self.y = y # the second cordinate of the center 
     # read-only    
    @property 
    def area (self):
        return  

    @property 
    def parimeter(self):
        return  
    @property
    def translate( self, dx , dy ):
        self.x += dx
        self.y += dy 

    @property 
    def center(self):
        return(self.x, self.y)   

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
    

    