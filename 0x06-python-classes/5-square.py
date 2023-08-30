#!/usr/bin/python3
'''
    A class Square that defines a square by:
    (based on 4-square.py)
'''


class Square:
    def __init__(self, size=0):

        '''
            Initializing this square class

            Args:
                size: represnets the size of the square defined
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

    @property
    def size(self):
        '''
            Retrieves size of square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            '''
                Raises:
                    TypeError: if size is not int
            '''
            raise TypeError('size must be an integer')
        if value < 0:
            '''
                Raises:
                    ValueError: if size < 0
            '''
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''
            Calculate area of the square
            Returns: The square of the size
        '''
        Area = self.__size * self.__size

        return Area

    def my_print(self):
        '''
            print the square in #
        '''

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
