#!/usr/bin/python3
'''
    A class Square that defines a square by:
    (based on 4-square.py)
'''


class Square:
    '''
        Instantiation with optional size
    '''

    def __init__(self, size=0):
        '''
            raises:
                TypeError: size must be an int
                ValueError: if size < 0
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        '''
            property to retrieve
        '''
        return self.__size

    @size.setter
    '''
        property setters for size
    '''
    def size(self, value):
        '''
            Raises:
                TypeError: size must be int
                ValueError: if size  < 0
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''
            Area of the square
        '''
        Area = (self.__size * self.__size)
        return Area

    def my_print(self):
        '''
            Prints to standard output
        '''
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
