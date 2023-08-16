#!/usr/bin/python3
'''
    A function that returns a key
    with the biggest integer value.
'''


def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    key_value = (max(a_dictionary, key=a_dictionary.get))

    return (key_value)
