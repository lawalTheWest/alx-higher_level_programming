#!/usr/bin/python3
'''
    This class Rectangle inherits from the Base class
'''
from models.base import Base
'''
    A class Rectangle
'''


class Rectangle(Base):

    '''
        A Class Constructor
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            get the width property of the Rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Set the width of the Rectangle
        '''
        if not isinstance(value, int):
            '''Raise a TypeError'''
            raise TypeError('width must be an integer')
        if value <= 0:
            '''
                raise ValueError
            '''
            raise ValueError('width must be > 0')

    @property
    def height(self):
        '''
            get the height of the Rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            set the height of the Rectangle
        '''
        if not isinstance(value, int):
            '''
                raise a TypeError
            '''
            raise TypeError('height must be an integer')
        if value <= 0:
            '''
                raise a ValueError
            '''
            raise ValueError('height must be > 0')

    @property
    def x(self):
        '''
            Get's the x value
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            Sets the  x value for the rectangle
        '''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            '''
                raise ValueError
            '''
            raise ValueError('x must be >= 0')

    @property
    def y(self):
        '''
            Gets the value of y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            Sets the value of y
        '''
        if not isinstance(value, int):
            '''Raise TypeError'''
            raise TypeError('y must be an integer')
        if value < 0:
            '''Raise ValueError'''
            raise ValueError('y must be >= 0')
