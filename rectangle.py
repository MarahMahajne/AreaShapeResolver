from shape import Shape

class Rectangle(Shape):
    """
    Rectangle shape class inheriting from Shape
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        """
        Method to calculate the area of the rectangle.
        """
        return self.length * self.width

    def __str__(self):
        """
        String casting for the Rectangle (In case of print for example)
        """
        return f"{super().__str__()}, Length: {self.length}, Width: {self.width}, Area: {self.get_area()}"
