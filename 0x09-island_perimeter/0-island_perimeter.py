#!/usr/bin/python3
"""
a function that returns the perimeter of the island.
"""


def island_perimeter(grid):
    """
    Island Perimeter Method
    """
    visit = set()
    per = 0

    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[i]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0

        visit.add((i, j))
        per = dfs(i, j + 1)
        per += dfs(i + 1, j)
        per += dfs(i, j - 1)
        per += dfs(i - 1, j)
        return per

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                return dfs(i, j)
