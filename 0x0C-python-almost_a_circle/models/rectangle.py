#!/usr/bin/python3
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
        self.width == width
        self.height == height
        self.x == x
        self.y == y

    def int_validator(self, key, value):
        """ the validator function """
        if not isinstance(value, int):
            raise TypeError(key + " must be an integer")
        elif key is "width" or key is "height":
            if value <= 0:
                raise ValueError(key + " must be > 0")
        elif key is "x" or key is "y":
            if value < 0:
                raise ValueError(key + " must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.int_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.int_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.int_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.int_validator("y", value)
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
