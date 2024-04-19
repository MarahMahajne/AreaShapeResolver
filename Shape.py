class Shape:
    """
    Base class for geometrical shapes.
    """
    
     def validate_input(self, inp):
        """
        validates the input of the objects.
        """
        try:
            float(inp)
            if inp > 0: 
                return True
            print("invalid input for the ",self.__class__,"object")
            return False
        except:
            print("invalid input for the ",self.__class__,"object")
            return False
            
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
