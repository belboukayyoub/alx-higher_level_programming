#!/usr/bin/python3
add = __import__("add_0").add


if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(1, 2, add(1, 2)))
