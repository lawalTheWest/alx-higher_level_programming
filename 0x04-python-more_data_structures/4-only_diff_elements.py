#!/usr/bin/python3
'''
    A function that returns a set of
    all elements present in only one set.
'''


def only_diff_elements(set_1, set_2):
    only_a_set = set_1 ^ set_2
    return (only_a_set)
