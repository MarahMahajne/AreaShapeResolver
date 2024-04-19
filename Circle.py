from Shape import Shape
from math import pi

class Circle(Shape):
    """
    Sub class for geometrical shapes.
    """
    def __init__( self, r ):
        """
        Constarts a Circle and checks the input.
        """
        if (super().validate_input(r)):
            self.radius = r
        else: 
            self.radius = 0

    def get_area(self):
        """
        Method to calculate the area of a Circle.
        """
        return (self.radius**2)*pi
    
    def __str__(self):
        """
        String representation of the Circle.
        """
        return "The radius of the circle is "+str(self.radius)
