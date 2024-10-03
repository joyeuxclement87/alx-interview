#!/usr/bin/python3
"""just working on the function that returns a list
of lists of integers representing the Pascal’s triangle
"""
def pascal_triangle(num):
    """this is the function to returns a list of lists of int
       that representing the Pascal’s triangle
    """
    value = []
    if (num <= 0):
        return value
    value.append([1])
    for a in range(num - 1):
        value.append([1] + [value[a][b] + value[a][b + 1]
                    for b in range(len(value[a]) - 1)] + [1])
    return value
