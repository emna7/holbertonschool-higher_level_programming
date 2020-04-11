#!/usr/bin/python3
""" Test function find_peak """
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    length = len(list_of_integers)
    if length == 1 or length == 2:
        if length == 2:
            if list_of_integers[0] > list_of_integers[1]:
                return list_of_integers[0]
            else:
                return list_of_integers[1]
    arr = list_of_integers
    peak = arr[0]
    for i in range(len(arr)):
        if arr[i+1] > arr[i]:
            peak = arr[i+1]
        return peak
