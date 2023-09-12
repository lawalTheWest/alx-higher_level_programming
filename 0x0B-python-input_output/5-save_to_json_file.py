#!/usr/bin/python3
'''This module defines a JSON file-writing function'''

import json


def save_to_json_file(my_obj, filename):
    '''Writes an object to a text file using JSON format'''
    with open(filename, 'w') as my_dict:
        json.dump(my_obj, my_dict)
