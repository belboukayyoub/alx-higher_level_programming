#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for c in my_string:
        if c not in 'cC':
            new += c
    return new
