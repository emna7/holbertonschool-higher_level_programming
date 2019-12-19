#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = my_dict.copy()
    for y, z in copy.items():
        if value in z:
            del my_dict[y]
    return my_dict
