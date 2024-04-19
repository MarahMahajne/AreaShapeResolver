from Rectangle import Rectangle

class Triangle(Rectangle):
    """
    Triangle shape inheriting from Rectangle
    """
    def __init__(self, length, width):
        super().__init__(length, width)

    def get_area(self):
        """
        Method to calculate the area of the triangle.
        """
        return super().get_area() / 2

    def __str__(self):
        """
        String representation of the Triangle.
        """
        return f"{super().__str__()}, Height: {self.height}, Width: {self.width}, Area: {self.get_area()}"
