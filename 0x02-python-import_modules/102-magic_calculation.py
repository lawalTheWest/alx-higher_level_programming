#!/usr/bin/python3
'''Convert bytecodes'''
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a > b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, 1)
            return (c)
    else:
        return (sub(a, b))
