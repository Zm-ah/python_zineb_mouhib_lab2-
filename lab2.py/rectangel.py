class Rectangle: # creat rec. class 
    def __init__(self, width , height , x = 0, y = 0 ):
        self._width = width 
        self._height = height 
        self.x = x
        self.y = y 

# read-only proprerty 
    @property    
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width * self.height) 
     
    #@property 
    #def center(self):
     #   return(self.x, self.y)
    
     
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
    
    # translation method, i will use this method to move the r. through the axes x,y
    def translate(self,dx , dy ):
        self.dx = dx 
        self.dy = dy 



