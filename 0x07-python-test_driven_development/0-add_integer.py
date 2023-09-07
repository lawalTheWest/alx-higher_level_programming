#!/usr/bin/python3
'''
    this function adds two numbers (int a, int b)
'''


def add_integer(a, b=98):
    # a must be an integer ELSE raise TypeError
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')

    # b must be an integer ELSE raise TypeError
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    # typecast a to int from float
    if isinstance(a, float):
        a = int(a)

    # typecast b to int from float
    if isinstance(b,float):
        b = int(b)

    # Return the sum of a and b = (int)
    sum = a + b
    return sum
