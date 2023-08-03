#!/usr/bin/python3
"""
A solution to the N queens problem
"""

import sys


def nqueens(n):
    """
    Solves the N queens problem
    """

    if n < 4:
        print("N must be at least 4")
        exit(1)

    bd = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(board, row, col):
        """
        Checks if a queen can be placed on board at row, col
        """

        # Check row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, col):
        """
        Solves the N queens problem
        """

        if col == n:
            solution = []

            for row in range(n):
                for col in range(n):
                    if board[row][col] == 1:
                        solution.append([row, col])

            solutions.append(solution)
            return True

        res = False

        # Consider this column and try placing this queen in all rows
        # one by one
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1

                res = solve(board, col + 1) or res

                board[i][col] = 0

        return res

    solve(bd, 0)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    nqueens(num)
