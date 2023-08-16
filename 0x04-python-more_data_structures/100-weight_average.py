#!/usr/bin/python3
'''
     a function that returns the weighted average
     of all integers tuple (<score>, <weight>)
'''


def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for _tuple in my_list:
        num += _tuple[0] * _tuple[1]
        den += _tuple[1]

    return (num / den)
