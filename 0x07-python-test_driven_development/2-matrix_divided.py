#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix, elements must be
    int or float type
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        return matrix
    if div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError('Each row of the matrix must have the same size')
            return matrix
