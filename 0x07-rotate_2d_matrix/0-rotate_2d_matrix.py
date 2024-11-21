#!/usr/bin/python3
"""
working to rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """to rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for a in range(int(n / 2)):
        y = (n - a - 1)
        for j in range(a, y):
            x = (n - 1 - j)
            # this is current number
            tmp = matrix[a][j]
            # this to change to the top for left
            matrix[a][j] = matrix[x][a]
            # tis to change left for bottom
            matrix[x][a] = matrix[y][x]
            # this to change bottom for right
            matrix[y][x] = matrix[j][y]
            # this to change right for top
            matrix[j][y] = tmp
