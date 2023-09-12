#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Defines a class MyList."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
