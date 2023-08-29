#!/usr/bin/python3
import sys
'''
    A function that executes a function safely.
'''


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
