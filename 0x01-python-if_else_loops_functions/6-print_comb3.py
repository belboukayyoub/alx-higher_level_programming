#!/usr/bin/python3
for num in range(1, 90):
    print("{:02d}".format(num), end=', ' if num < 89 else '\n')
