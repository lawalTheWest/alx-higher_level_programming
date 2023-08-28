#!/usr/bin/python3
'''
    A function that prints x elements of a list.
'''



def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements_printed += 1
        except:
            break
    print("")
    return (elements_printed)
