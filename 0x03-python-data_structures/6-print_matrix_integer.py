#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        separ = ''
        for col in row:
            print("{}{:d}".format(separ, col), end='')
            separ = ' '
        print()
