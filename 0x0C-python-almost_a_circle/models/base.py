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

    @staticmethod
    def from_json_string(json_string):
        '''
             returns:
                A list of JSON string representation json_string
            json_string is a string
                representing a list of dictionaries.
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        '''
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            Return:
                an Instantiated class from a dictionary of attributes.
            @**dictionary: attribute to instatiate
        '''
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        '''
        '''
        filename = str(cls.__name__) + '.json'
        try:
            with open(filename, 'r+') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_tofile_csv(cls, list_objs):
        '''
            Write the CSV serialization of a list of objects to a file
            list_objs: A list of inherited Base instances
        '''
        filename = cls.__name__ + '.csv'
        with open(filename, 'w+', newline='') as csvfile:
            if list_onjs is None or list_objs == []:
                csvfile.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    filenames = ['id', 'width', 'height', 'x', 'y']
                else:
                    filenames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''
            Return a list of classes instantiated from a CSV file.
        '''

