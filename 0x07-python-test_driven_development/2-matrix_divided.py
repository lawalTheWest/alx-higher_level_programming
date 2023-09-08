#!/usr/bin/python3
"""
    A function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """
        Function that divides the integer/float numbers 
        of a matrix
    """

    if not type(div) in (int, float):
        '''
            raise TypeError if matrix is not
            a list of lists of integers or floats
        '''
        raise TypeError("div must be a number")

    if div == 0:
        '''raise a ZeroDivisionError'''
        raise ZeroDivisionError("division by zero")

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)
    
    lenght = 0
    msg2 = "Each row of the matrix must have the same size"

    for elements in matrix:
        '''matrix mmust be a list'''
        if not elements or not isinstance(elements, list):
            raise TypeError(msg1)

        '''validating data type'''
        if lenght != 0 and len(elements) != lenght:
            raise TypeError(msg2)

        '''type validation'''
        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        lenght = len(elements)
        new_mat = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (new_mat)
