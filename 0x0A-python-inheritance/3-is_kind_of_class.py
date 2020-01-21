#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    if issubclass(type(obj), a_class):
        return True
    return False
