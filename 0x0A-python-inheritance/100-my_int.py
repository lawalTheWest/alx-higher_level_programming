#!/usr/bin/python3
'''
    This defines a class MyInt
    that inherits from int.
'''


class MyInt(int):
    '''Invert int operators == and !=.'''

    def __eq__(self, value):
        '''== opeartor is rabelled with !='''
        return self.real != value

    def __ne__(self, value):
        '''!= operator is rabelled with =='''
        return self.real == value
