from Shape import Shape
from math import sqrt

class Hexagon(Shape):
    """
    Sub class for geometrical shapes.
    """
    def __init__( self, t ):
        """
        Constarts a Hexagon and checks the input.
        """
        if super().validate_input(t):
            self.side = t
        else: 
            self.side = 0

    def get_area(self):
        """
        Method to calculate the area of a Hexagon.
        """
        return (self.side**2)*3*sqrt(3)/2
    
    def __str__(self):
        """
        String representation of the Hexagon.
        """
        return "The side of the hexagon is "+str(self.side)
