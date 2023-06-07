#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in str:
        if 'a' <= c <= 'z':
            new_str += "{:c}".format(ord(c) + ord('A') - ord('a'))
        else:
            new_str += c
    print(new_str)
