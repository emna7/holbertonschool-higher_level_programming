#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        super(Rectangle, self).__init__()
        self.__size = self._Rectangle__width = self._Rectangle__height = size

    def area(self):
        return self.__size ** 2
