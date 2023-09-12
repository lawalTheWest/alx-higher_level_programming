#!/usr/bin/python3
'''This module defines a file-writing function.'''

def write_file(filename="", text=""):
    '''
        Writes a string to a UTF8 text file
    '''
    with open(filename, 'w', encoding='utf-8') as my_first_file:
        return my_first_file.write(text)
