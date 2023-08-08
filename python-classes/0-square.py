class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The private attribute representing the side length of the square.

    Methods:
        __init__(self, size):
            Initializes a new Square instance with the given size.

    Usage:
        my_square = Square(3)
        print(type(my_square))  # <class 'Square'>
        print(my_square.__dict__)  # {'_Square__size': 3}

        # Attempting to access private attributes will raise AttributeError
        try:
            print(my_square.size)  # Raises AttributeError
        except AttributeError as e:
            print(e)

        try:
            print(my_square.__size)  # Raises AttributeError
        except AttributeError as e:
            print(e)
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The side length of the square.

        Note:
            This constructor initializes the private attribute __size with the provided size.
        """
        self.__size = size
