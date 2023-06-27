#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for nbr in my_list:
        try:
            if counter == x:
                break
            print("{:d}".format(nbr), end="")
            counter += 1
        except (TypeError, ValueError):
            continue
    print("")
    return counter
