#!/usr/bin/python3
"""
function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n:
    - Returns an empty list if n <= 0
    - You can assume n will be always an integer
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    res = [[1]]
    for i in range(n - 1):
        tmp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        res.append(row)
    return res
