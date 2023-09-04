#!/usr/bin/python3
'''
    A class Rectangle that defines a rectangle by:
    (based on 0-rectangle.py)
'''


class Rectangle:
    '''defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''
            Instantiation
            Args:
                width: width of triangle
                height: height of triangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''To retrieve width of rectangle'''
        return sellf.__width

    @width.setter
    def width(self, value):
        '''To set width of rectangle'''

        if not isinstance(value, int):
            '''checking if value is intiger'''
            raise TypeError('width must be an integer')

        if value < 0:
            '''checking if Value is not Negative'''
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
            '''To validate if  value is int'''
            raise TypeError('height must be an integer')

        if value < 0:
            '''to validate if value is > 0'''
            raise ValueError('height must be an integer')
        self.__height = value
