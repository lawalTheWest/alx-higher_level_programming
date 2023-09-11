#!/usr/bin/python3
'''
    Contains definiton for the class MyList
    this also inherits from list.
'''


class MyList(list):
    '''
        defines the class MyList and inherit from list.
    '''

    def print_sorted(self):
        '''Prints list elements(int) in ascending order'''

        sorted_list = sorted(self)
        print(sorted_list)
