#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./nqueens.py N

N must be an integer greater than or equal to 4.
"""

import sys


def initialize_board(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def is_safe(board, row, col):
    """Check if it's safe to place a queen at a given position."""
    n = len(board)

    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True


def recursive_solve(board, row, solutions):
    """Recursively solve the N-queens puzzle."""
    n = len(board)

    if row == n:
        solutions.append([[r, c] for r in range(n)
                         for c in range(n) if board[r][c] == 'Q'])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            recursive_solve(board, row + 1, solutions)
            board[row][col] = ' '


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = initialize_board(n)
    solutions = []
    recursive_solve(board, 0, solutions)

    for solution in solutions:
        print(solution)
