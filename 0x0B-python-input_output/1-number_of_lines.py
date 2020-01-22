#!/usr/bin/python3
def number_of_lines(filename=""):
    nb = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            nb += 1
    return nb
