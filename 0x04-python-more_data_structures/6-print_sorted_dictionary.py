#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for y in sorted(my_dict.keys()):
        print("{}: {}".format(y, my_dict[y]))
