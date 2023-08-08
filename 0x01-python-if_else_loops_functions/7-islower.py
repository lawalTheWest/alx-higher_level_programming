#!/usr/bin/python3
def islower(c):
    """This Function checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        # using the code point for each letter
        return (True)
    else:
        return (False)
