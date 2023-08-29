#!/usr/bin/python3
'''
    A class Square that defines a square by:
    (based on 2-square.py)
'''


class Square:
    '''
        Defines a square class
    '''
    def __init__(self, size=0):
        '''
            instantiation with optional size
        '''
        if not isinstance(size, int):
            '''
                Raises:
                    TypeError: if size is not int
            '''
            raise TypeError('size must be an integer')

        if size < 0:
            '''
                Raises:
                    ValueError: if size < 0
            '''
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        '''
            Return: Area of the square
        '''
        Area = (self.__size * self.__size)
        return Area
