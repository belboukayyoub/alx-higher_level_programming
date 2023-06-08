#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1
    print(f"{num_args} argument{'s' if num_args != 1 else ''}\
{'.' if num_args == 0 else ':'}")
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        print(f"{i}: {arg}")
