#!/usr/bin/python3
'''a function that returns a
    tuple with the length of
    a string and its first character.'''


def multiple_returns(sentence):
    lenght = len(sentence)
    if sentence:
        first_char = sentence[0]
        return (lenght, first_char)
    else:
        first_char = None
        return (lenght, first_char)
