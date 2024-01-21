#!/usr/bin/python3
"""
This module contains a function
"""


def minOperations(n):
    """
    Calculate the fewest number of operations
    `n` 'H' characters in the file.

    Parameters:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The minimum number of operations.
    return 0.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i + minOperations(n//i)
        return n
