#!/usr/bin/python3
"""inherit a class from a subclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
