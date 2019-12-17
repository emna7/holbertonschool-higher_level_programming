#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        no_cstring = ""
        for a in my_string:
            if a != 'C' and a != 'c':
                no_cstring += a
        return no_cstring
    else:
        return my_string
