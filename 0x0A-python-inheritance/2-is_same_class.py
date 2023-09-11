#!/usr/bin/python3
'''
    This Defines a class-checking function
'''


def is_same_class(obj, a_class):
    '''
        This function Checks
        if an object is exactly an instance
        of a given class.
        Args:
            @obj: The object to check.
            @a_class: The class to match the type of obj to.
        Returns:
            If obj is exactly an instance of a_class - True.
            Otherwise - False.
    '''
    if type(obj) == a_class:
        '''If the object is an instance of the class type'''
        return True
    return False
