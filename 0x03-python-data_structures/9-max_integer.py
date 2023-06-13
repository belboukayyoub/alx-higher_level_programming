#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        _max = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > _max:
                _max = my_list[i]
        return _max
    return None
