#!/usr/bin/python3
""" Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ rectangle class - inherits from Base
    Attributes:
        width (obj:`int`): width of rectangle
        height (obj:`int`): height of rectangle
        x (obj:`int`): x set of rectangle
        y (obj:`int`): y set of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ the init function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def int_validator(self, key, value):
        """ the validator function """
        if not isinstance(value, int):
            raise TypeError(key + " must be an integer")
        elif key == "width" or key == "height":
            if value <= 0:
                raise ValueError(key + " must be > 0")
        elif key == "x" or key == "y":
            if value < 0:
                raise ValueError(key + " must be >= 0")

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area function """
        return self.__width * self.__height

    def display(self):
        """ display function """
        if self.__y > 0:
            print("\n" * (self.__y), end="")
        for c in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ str function """
        return (
            "[Rectangle] (" + str(self.id) + ") " +
            str(self.__x) + "/" + str(self.__y) + " - " +
            str(self.__width) + "/" + str(self.__height)
        )

    def update(self, *args, **kwargs):
        """ update function """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for att, arg in zip(attributes, args):
                setattr(self, att, arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ the dict function """
        dict = {}
        dict['id'] = self.id
        dict['width'] = self.width
        dict['height'] = self.height
        dict['x'] = self.x
        dict['y'] = self.y
        return dict
