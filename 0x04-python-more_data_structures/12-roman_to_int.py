#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or \
       len(roman_string) == 0 or \
       roman_string is None:
        return 0
    result = 0
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    for idx, c in enumerate(roman_string):
        if c not in convert:
            return 0
        if (idx + 1) == len(roman_string) or \
           convert[c] >= convert[roman_string[idx+1]]:
            result += convert[c]
        else:
            result -= convert[c]
    return result
