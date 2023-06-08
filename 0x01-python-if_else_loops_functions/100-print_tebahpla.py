#!/usr/bin/python3
for i in range(26, 0, -1):
    print("{:c}".format(i + 96 if i % 2 == 0 else i + 64), end='')
