#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename) as f:
        i = len(list(f))
        if nb_lines >= i or nb_lines <= 0:
            nb_lines = i
        f.seek(0, 0)
        for count in range(nb_lines):
            print(f.readline(), end="")
