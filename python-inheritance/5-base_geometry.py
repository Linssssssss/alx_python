#!/usr/bin/python3
"""
Module contains the `BaseGeometry` class
"""


class BaseGeometry():
    """
    The BaseGeometry class
    """

    def area(self):
        """
        raises the exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
