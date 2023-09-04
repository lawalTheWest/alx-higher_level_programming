#!/usr/bin/python3
'''
    class to Define a Rectangle.
'''


class Rectangle:
    '''Represent a rectangle.'''

    def __init__(self, width=0, height=0):
        '''
            Initialize a new Rectangle.
            Args:
                width: width of the new rectangle.
                height: height of the new rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieves the width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width of the triangle'''
        if not isinstance(value, int):
            raise TypeError('width must be an intege')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''retrieves the height of the Rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height of rectangle'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
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
        height_side =  self.__height * 2
        perimeter = width_side + height_side
        return perimeter

    def __str__(self):
        '''
            Return printed rectangle with the # character.
        '''
        if self.__width == 0 or self.__height == 0:
            return ('')

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return (''.join(rect))

    def __repr__(self):
        '''
            Return the string representation
            of the Rectangle.
        '''
        rect = 'Rectangle(' + str(self.__width)
        rect += ', ' + str(self.__height) + ')'
        return (rect)

    def __del__(self):
        '''
            Print a message
            for every deletion of a Rectangle.
        '''
        print('Bye rectangle...')
