class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The private attribute representing the side length of the square.

    Methods:
        __init__(self, size=0):
            Initializes a new Square instance with the given size.

    Usage:
        # Creating a square instance with default size (0)
        square_default = Square()
        print(square_default.__dict__)  # {'_Square__size': 0}

        # Creating a square instance with size 3
        square_with_size = Square(3)
        print(square_with_size.__dict__)  # {'_Square__size': 3}

        # Attempting to create a square instance with invalid size
        try:
            invalid_square = Square("invalid")
        except TypeError as e:
            print(e)  # Output: size must be an integer

        try:
            negative_square = Square(-2)
        except ValueError as e:
            print(e)  # Output: size must be >= 0
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int, optional): The side length of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
