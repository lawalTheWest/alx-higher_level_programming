#!/usr/bin/python3
"""
    This module returns the list
    of available attributes
    and methods of an object
    Args:
        @obj: the object
"""


def lookup(obj):
    '''This returns a list of an object's available attributes.'''
    return (dir(obj))
