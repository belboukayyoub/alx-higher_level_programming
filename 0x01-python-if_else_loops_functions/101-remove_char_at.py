#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    for i in range(0, len(str)):
        if i != n:
            cpy += str[i]
    return cpy
