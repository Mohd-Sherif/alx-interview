#!/usr/bin/python3
"""
A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Minimum Operations
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factorize n by dividing it by the smallest divisor
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
