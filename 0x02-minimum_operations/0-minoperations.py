#!/usr/bin/python3

"""
    working with the method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        this is a function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    """

    n = 1
    st = 0
    cnt = 0
    while n < n:
        rm = n - n
        if (rm % n == 0):
            st = n
            n += st
            cnt += 2
        else:
            n += st
            cnt += 1
    return cnt
