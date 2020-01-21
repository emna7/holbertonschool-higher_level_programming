#!/usr/bin/python3


class MyInt(int):
    def __init__(self, a):
        self.a = a

    def __ne__(self, b):
        return (self.a == b)

    def __eq__(self, b):
        return self.a != b
