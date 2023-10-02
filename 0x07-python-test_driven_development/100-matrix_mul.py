#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices."""


def matrix_mul(m_a, m_b):
    """Multiply 2 matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Returns:
        A matrix of the multiplication of m_a by m_b.
    """

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    # variables to verify if both m_a and m_b can be multiplied
    num_colum = 0
    num_row = 0

    # Check requirements for matrix m_a
    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row in m_a:
        if type(row) != list:
            raise TypeError("m_a must be a list of lists")
        _len = len(m_a[0])
        if row == []:
            raise ValueError("m_a can't be empty")
        if _len != len(row):
            raise TypeError("each row of m_a must be of the same size")
        num_colum = len(row)
        for column in row:
            if type(column) != int and type(column) != float:
                raise TypeError("m_a should contain only integers or floats")

    # Check requirements for matrix m_b
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row in m_b:
        if type(row) != list:
            raise TypeError("m_b must be a list of lists")
        _len = len(m_b[0])
        if row == []:
            raise ValueError("m_b can't be empty")
        if _len != len(row):
            raise TypeError("each row of m_b must be of the same size")
        num_row += 1
        for column in row:
            if type(column) != int and type(column) != float:
                raise TypeError("m_b should contain only integers or floats")

    # Check if the multiplication is posible
    if num_colum != num_row:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for row in m_a:
        i = 0
        new_row = []
        while i < len(m_b[0]):
            result = 0
            j = 0
            for column in row:
                result += column * m_b[j][i]
                j += 1
            new_row.append(result)
            i += 1
        mul_matrix.append(new_row)

    return mul_matrix
