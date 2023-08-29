#!/usr/bin/python3
'''
    A function that divides 2 integers and prints the result.
'''


def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
