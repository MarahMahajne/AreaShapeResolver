from Shape import Shape

class Square(Shape):
    """
    Class representing a square.
    """
    def __init__(self, side_length):
        """
        Constructor for Square class and checks the input.
        """
        if super().validate_input(side_length):
            self.side_length = side_length
        else: 
            self.side_length = 0

    def get_area(self):
        """
        Calculate the area of the square.

        Returns:
        float: The area of the square.
        """
        return self.side_length ** 2

    def __str__(self):
        """
        String representation of the square.

        Returns:
        str: String representation of the square.
        """
        return f"This is a Square with side length {self.side_length}"
