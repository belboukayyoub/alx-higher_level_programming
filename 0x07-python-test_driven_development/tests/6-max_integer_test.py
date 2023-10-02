#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for the function def max_integer(list=[])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_integer(ordered), 6)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [6, 1, 4, 5, 2, 3]
        self.assertEqual(max_integer(unordered), 6)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [6, 5, 4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 6)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [8]
        self.assertEqual(max_integer(one_element), 8)

    def test_floats(self):
        """Test a list of floats."""
        floats = [5.35, 7.77, -1.02, 20.20, 1.0, 20.21]
        self.assertEqual(max_integer(floats), 20.21)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [5.35, 7, -1.02, -20.20, 1.0, 20]
        self.assertEqual(max_integer(ints_and_floats), 20)

    def test_string(self):
        """Test a string."""
        string = "Belbouk"
        self.assertEqual(max_integer(string), 'u')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["I'm", "so", "happy", "to", "join", "ALX"]
        self.assertEqual(max_integer(strings), "to")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
