#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list) > 0:
        num, div = 0, 0
        for tp in my_list:
            num += tp[0] * tp[1]
            div += tp[1]
        return num / div
    return 0
