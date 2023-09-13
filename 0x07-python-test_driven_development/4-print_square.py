#!/usr/bin/python3
'''
    A function that prints a square with the character #.
'''


def print_square(size):
    '''
        Args:
            size: The size length of the square(integer).
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    # end if
    elif size < 0:
        raise ValueError('size must be >= 0')
    # end elif
    else:
        for i in range(size):
            print('{}'.format('#' * size))
    # end else
