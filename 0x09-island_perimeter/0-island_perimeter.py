#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    p = 0
    for a in range(len(grid)):
        for k in range(len(grid[a])):
            if (grid[a][k] == 1):
                if (a <= 0 or grid[a - 1][k] == 0):
                    p += 1
                if (a >= len(grid) - 1 or grid[a + 1][k] == 0):
                    p += 1
                if (k <= 0 or grid[a][k - 1] == 0):
                    p += 1
                if (k >= len(grid[a]) - 1 or grid[a][k + 1] == 0):
                    p += 1
    return p
