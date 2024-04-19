from Shape import Shape

class Rectangle(Shape):
    """
    Rectangle shape class inheriting from Shape
    """
    def __init__(self, height, width):
        """
        Constarts a Rectangle and checks the input.
        """
        if super().validate_input(height) and super().validate_input(width):
            self.height = height
            self.width = width        
        else: 
            self.height = 0
            self.width = 0

    def get_area(self):
        """
        Method to calculate the area of the rectangle.
        """
        return self.height * self.width

    def __str__(self):
        """
        String casting for the Rectangle (In case of print for example)
        """
        return f"{super().__str__()}, Height: {self.height}, Width: {self.width}, Area: {self.get_area()}"
