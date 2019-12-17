#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        b = ""
        for j in range(len(matrix[i])):
            print(b, end="")
            print("{:d}".format(matrix[i][j]), end="")
            b = " "
        print()
