#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        # Printing excluding comma
        print('{}'.format(number))
    else:
        # printing comma inclusive
        print('{:02}'.format(number), end=', ')
