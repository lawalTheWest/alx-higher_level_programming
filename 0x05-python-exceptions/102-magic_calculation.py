#!/usr/bin/python3
'''
    Python function def magic_calculation(a, b):
    that does exactly the same as
    the given Python bytecodes
'''


def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += a ** b / i
        except:
            result = a + b
            break
    return result
