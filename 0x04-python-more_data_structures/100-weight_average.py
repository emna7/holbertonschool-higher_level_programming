#!/usr/bin/python3
def weight_average(my_list=[]):
    y = x = 0
    if my_list and len(my_list):
        for t in my_list:
            x += t[0] * t[1]
            y += t[1]
        return x / y
    return 0
