#!/usr/bin/python3
'''A class Rectangle that defines a rectangle by:'''


class Rectangle:
    '''defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''
            Instantiation
            Args:
                width: width of triangle
                height: height of triangle
        '''
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''To retrieve width of rectangle'''
        return sellf.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''To retrieve height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''To set height of rectangle'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be an integer')
        self.__height = value
