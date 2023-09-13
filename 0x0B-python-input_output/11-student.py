#!/usr/bin/python3
'''This module defines a class Student'''


class Student:
    '''Represent a student.'''

    def __init__(self, first_name, last_name, age):
        '''
            Initializes a new Student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
            This gets a dictionary representation of the Student.
            If attrs is a list of strings:
                represents only those attributes
            included in the list
        '''
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        '''
            Replaces all attributes of the Student
        '''
        for b, c in json.items():
            setattr(self, b, c)
