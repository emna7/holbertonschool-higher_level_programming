#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    to_print = ""
    characters = ['.', '?', ':']
    for string in text:
        to_print += string
        if string in characters:
            to_print += "\n\n" 
            print(to_print, end='')
