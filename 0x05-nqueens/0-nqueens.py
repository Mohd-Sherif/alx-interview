#!/usr/bin/python3
"""
A program that solves the N queens problem.
"""

import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def nqueens(N):
    solutions = []
    board = [-1] * N
    solve(N, 0, board, solutions)
    for solution in solutions:
        print(solution)


def solve(N, row, board, solutions):
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(N, row + 1, board, solutions)
                board[row] = -1


def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)


if __name__ == "__main__":
    main()
