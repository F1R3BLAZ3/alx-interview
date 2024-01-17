#!/usr/bin/python3
"""
This script defines a method minOperations that calculates the
fewest number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    :param n: Target number of H characters
    :return: Number of operations, or 0 if impossible
    """
    if n <= 1:
        return 0

    # Initialize the list to store the minimum number of operations for each position
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
