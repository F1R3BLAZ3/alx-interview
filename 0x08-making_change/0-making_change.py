#!/usr/bin/python3
"""
This module provides the makeChange function which determines
the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The amount total.

    Returns:
        int: The fewest number of coins needed to meet the total,
             or -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
