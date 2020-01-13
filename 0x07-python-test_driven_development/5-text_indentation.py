#!/usr/bin/python3
def text_indentation(text):
    """
    prints a string of text with 2 new lines after '.', '?', and ':'
    unit tests located in tests/5-text_indentation.txt
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    to_print = ""
    characters = ['.', '?', ':']
    for string in text:
        to_print += string
        if string in characters:
            to_print += "\n\n" 
            print(to_print, end='')
