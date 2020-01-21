#!/usr/bin/python3
def inherits_from(obj, a_class):
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    return False
