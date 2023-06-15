#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda elm: elm if elm != search else replace, my_list))
