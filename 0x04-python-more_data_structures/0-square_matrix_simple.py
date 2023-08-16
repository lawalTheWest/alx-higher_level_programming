#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    lenght = len(matrix)

    for i in range(lenght):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
