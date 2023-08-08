#!/usr/bin/python3
class Square:
    """Square class"""

    def __init__(self, size):
        """Initialize square with size"""
        self.__size = size

    def area(self):
        """Compute the area of the square"""
        return self.__size * self.__size
