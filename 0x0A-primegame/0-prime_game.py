#!/usr/bin/python3
"""working on the 0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """this is x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    maria = 0
    ben = 0

    m = [1 for x in range(sorted(nums)[-1] + 1)]
    m[0], m[1] = 0, 0
    for a in range(2, len(m)):
        rm_multiples(m, a)

    for a in nums:
        if sum(m[0:a + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """working to removes multiple
    of primes
    """
    for a in range(2, len(ls)):
        try:
            ls[a * x] = 0
        except (ValueError, IndexError):
            break
