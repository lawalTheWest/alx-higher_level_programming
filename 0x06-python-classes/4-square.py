#!/usr/bin/python3
'''
    A class Square that defines a square by:
    (based on 3-square.py)
'''


class Square:
    '''
        Instantiation with optional size
    '''
    def __init__(self, size=0):

        if not isinstance(size, int):
            '''
            Raise:
                TypeError: if size is not int
            '''
            raise TypeError('size must be an integer')
        if size < 0:
            '''
                Raise:
                    ValueError: if size is < 0
            '''
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        '''
            Retrieve size
        '''

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            '''
                Raise:
                    TypeError: if size is not int
            '''
            raise TypeError('size must be an integer')

        if value < 0:
            '''
                Raise:
                    ValueError: if size is < 0
            '''
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        '''
            Area of the aquare
        '''
        Area = (self.__size * self.__size)
        return Area
