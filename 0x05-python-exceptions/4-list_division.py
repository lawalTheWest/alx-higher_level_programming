#!/usr/bin/python3
'''
    A function that divides element by element 2 lists.
'''

def list_division(my_list_1, my_list_2, list_length):
    div_result = []
    temp_holder = 0
    for i in range(0, list_length):
        try:
            temp_holder = my_list_1[i] / my_list_2[i]
        except TypeError:
            temp_holder = 0
            print("wrong type")
        except ZeroDivisionError:
            temp_holder = 0
            print("division by 0")
        except IndexError:
            temp_holder = 0
            print("out of range")
        finally:
            pass
        div_result.append(temp_holder)
    return div_result
