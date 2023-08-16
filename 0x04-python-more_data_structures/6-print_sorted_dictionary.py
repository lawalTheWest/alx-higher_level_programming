#!/usr/bin/python3
'''
    A function that prints a dictionary by ordered keys.
    Assume that all keys are strings
    Keys should be sorted by alphabetic order
    
    Only sort keys of the first level
    (don’t sort keys of a dictionary inside the main dictionary)
    
    Dictionary values can have any type
'''


def print_sorted_dictionary(a_dictionary):
    # to sort this array
    sort_dictionary = sorted(a_dictionary.keys())
    for key in sort_dictionary:
        print('{}: {}'.format(key, a_dictionary[key]))
