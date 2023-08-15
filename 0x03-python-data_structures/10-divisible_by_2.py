#!/usr/bin/python3
'''a function that finds all multiples of 2 in a list.'''


def divisible_by_2(my_list=[]):
    if my_list:
        return list(map(lambda n: not (n % 2), my_list))
    return None
