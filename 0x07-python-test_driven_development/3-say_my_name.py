#!/usr/bin/python3
'''
     A function that prints My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    '''
        Args:
            @first_name: The first name of the person(string).
            @last_name: The last name of the person(stroing).
        Raises:
            TypeError: If the first_name and last_name are not strings.
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    # end if
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    # end elif
    else:
        print('My name is {} {}'.format(first_name, last_name))
    # end else
