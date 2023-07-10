#!/usr/bin/python3
"""
Module for minOperations method.
"""


def minOperations(n):
    """
    Method that determines the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    operations = 0
    while n % 2 == 0:
        operations += 2
        n = n / 2
    divisor = 3
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n / divisor
        divisor += 2
    return operations
