class Shape:
    """
    Base class for geometrical shapes.
    """
    def get_area(self):
        """
        Abstract method to calculate the area of a shape.
        """
        raise NotImplementedError("Subclasses must implement get_area() method.")

    def __str__(self):
        """
        String representation of the shape.
        """
        return f"This is a {type(self).__name__}"
