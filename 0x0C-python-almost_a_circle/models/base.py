#!/usr/bin/python3
import json
'''
    Defines class Base:
        This class is the “base” of all other classes in this project
        The goal here is to manage id attribute,
            in all the future classes and
            to avoid duplicating the same code
'''


class Base:
    '''
        A private class attribute
    '''

    __nb_objects = 0

    '''
        A Class Constructor
        Args:
            @id: the id of the new class Base
    '''
    def __init__(self, id=None):
        if id is not None:
            '''
                Assign the public instance attribute id
                Assume "id" is an integer (we need not to test the type)
                    (id = integer)
            '''
            self.id = id
        else:
            '''
                Increment __nb_objects and
                Assign the new value to the public instance attribute id
            '''
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            Returns The JSON serialization of a list of dictionary
            Args:
                list_dictionaries(list): A list
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
             This writes the JSON string representation
             of list_objs to a file:
                - list_objs is a list of instances
                    who inherits of Base - example:
                        list of Rectangle or list of Square instances
                - If list_objs is None, save an empty list
                - The filename must be:
                    <Class name>.json - example:
                        Rectangle.json
                - must use the static method to_json_string
                    (created before)
                - must overwrite the file if it already exists
        '''
        filename = cls.__name__ + '.json'
        with open(filename, 'w+') as jsonfile:
            if list_objs is None:
                jsonfile.write('[]')
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
