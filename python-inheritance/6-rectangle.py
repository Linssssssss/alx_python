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


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
