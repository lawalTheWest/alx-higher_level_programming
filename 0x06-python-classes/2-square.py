#!/usr/bin/python3
'''
    A class Square that defines a square by:
    (based on 1-square.py)
'''


class Square:
    '''A class that defines a square'''

    def __init__(self, size=0):
        '''
            Initializing the square class
            arguments
            Args:
                size: size of square
            Raises:
                TypeError: if size is not an int
                ValueError: if size < 0

        '''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
