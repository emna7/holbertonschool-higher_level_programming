#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        s = my_list[0]
        for a in range(1, len(my_list)):
            if my_list[a] > s:
                s = my_list[a]
        return s
    else:
        return None
