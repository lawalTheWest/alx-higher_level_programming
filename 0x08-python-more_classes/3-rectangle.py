#!/usr/bin/python3
'''
    class to Defines a Rectangle class
'''


class Rectangle:
    '''Represent a rectangle.'''

    def __init__(self, width=0, height=0):
        '''
            Initialize a new Rectangle.
            Args:
                width: The width of the new rectangle.
                height: The height of the new rectangle.
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''Get/set the width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
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
        '''set the height of the Rectangle.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Return the area of the Rectangle.'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Return the perimeter of the Rectangle.'''
        if self.__width == 0 or self.__height == 0:
            return (0)

        width_side = self.__width * 2
        height_side = self.__height * 2
        perimeter = width_side + height_side
        return perimeter

    def __str__(self):
        '''
            Return: the rectangle with the # character.
        '''
        if self.__width == 0 or self.__height == 0:
            return ('')

        rectangle = []
        for val1 in range(self.__height):
            [rectangle.append('#') for val2 in range(self.__width)]
            if val1 != self.__height - 1:
                rectangle.append('\n')
        return (''.join(rectangle))
