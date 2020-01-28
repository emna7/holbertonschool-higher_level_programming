#!/usr/bin/python3
""" Square Class """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class, inheriting from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ init function """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ str function """
        string1 = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        string2 = "{}/{} ".format(self.x, self.y)
        string3 = "- {}".format(self.width)
        return(string1 + string2 + string3)

    @property
    def size(self):
        """ size property """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """ update function """
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for att, arg in zip(attributes, args):
                setattr(self, att, arg)
        elif kwargs:
            for att, arg in kwargs.items():
                if att in attributes:
                    setattr(self, att, arg)

    def to_dictionary(self):
        """ dict function """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
            }
