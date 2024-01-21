#!/usr/bin/python3
"""
This script defines a method minOperations that calculates the
fewest number of operations needed to result in exactly n H characters
in the file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters.

    :param n: Target number of H characters
    :return: Number of operations, or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations


# Example usage
if __name__ == "__main__":
    n = 19170307
    result = minOperations(n)
    print(f"Number of operations for n={n}: {result}")
