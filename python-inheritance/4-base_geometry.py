class BaseGeometry:
    def area(self):
        """Placeholder method for calculating the area of a shape."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is an integer and greater than 0."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
