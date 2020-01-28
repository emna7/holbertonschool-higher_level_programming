#!/usr/bin/python3
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
        return (
            "[Square] (" + str(self.id) + ") " +
            str(self.x) + "/" + str(self.y) +
            " - " + str(self.width)
            )

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
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
