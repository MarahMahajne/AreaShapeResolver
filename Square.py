from Rectangle import Rectangle

class Square(Rectangle):
    """
    Class representing a square inheriting from Rectangle.
    """
    def __init__(self, side_length):
        """
        Constructor for Square class.
        """
        super().__init__(side_length, side_length)


    def get_area(self):
        """
        Calculate the area of the square.

        Returns:
        float: The area of the square.
        """
        return super().get_area()

    def __str__(self):
        """
        String representation of the square.

        Returns:
        str: String representation of the square.
        """
        return f"This is a Square with side length {self.width}"
