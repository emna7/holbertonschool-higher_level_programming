#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode="w", encoding='UTF-8') as f:
        n = f.write(text)
    return n
