#!/usr/bin/python3

"""Class docstrings go here."""


class Square:
    """Class docstrings go here."""

    def __init__(self, size):
        """__init__ constructor method."""
        self.__size = size


if __name__ == "__main__":

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
