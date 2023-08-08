#!/usr/bin/python3
for value in range(ord('a'), ord('z') + 1):
    if chr(value) != 'e' and chr(value) != 'q':
        print('{:c}'.format(value), end='')
