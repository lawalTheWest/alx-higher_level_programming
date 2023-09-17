#!/usr/bin/python3
'''
    Defines class Base:
        This class is the “base” of all other classes in this project
        The goal here is to manage id attribute,
            in all the future classes and
            to avoid duplicating the same code
'''


class Base:
    '''
        A private class attribute
    '''

    __nb_objects = 0

    '''
        A Class Constructor
        Args:
            @id: the id of the new class Base
    '''
    def __init__(self, id=None):
        if id is not None:
            '''
                Assign the public instance attribute id
                Assume "id" is an integer (we need not to test the type)
                    (id = integer)
            '''
            self.id = id
        else:
            '''
                Increment __nb_objects and
                Assign the new value to the public instance attribute id
            '''
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
