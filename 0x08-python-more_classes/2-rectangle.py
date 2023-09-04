#!/usr/bin/python3
'''
    class Rectangle that defines a rectangle
'''


class Rectangle:
    '''A rectangle class.'''

    def __init__(self, width=0, height=0):
        '''
            Initializes a new Rectangle.
            Args:
                width (int): width of the new rectangle.
                height (int): height of the new rectangle.
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''retrieves the width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the Width of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Get the height of the Rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Return the area of the Rectangle.'''
        area = self.__width * self.__height
        return area

    def perimeter(self):
        '''Return the perimeter of the Rectangle.'''
        if self.__width == 0 or self.__height == 0:
            return 0

        width_side = self.__width * 2
        height_side = self.__height * 2
        perimeter = width_side + height_side
        return perimeter
