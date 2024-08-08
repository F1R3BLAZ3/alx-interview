#!/usr/bin/python3
"""
Module to determine the winner of the Prime Game between Maria and Ben.
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game after x rounds.

    Parameters:
    - x (int): The number of rounds to be played.
    - nums (list): A list of integers representing the upper limit
                   for each round.

    Returns:
    - str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more rounds,
    or None if it's a tie.
    """
    if x <= 0 or not nums:
        return None

    # Find the maximum value in nums to limit our sieve
    max_num = max(nums)

    # Create a sieve to determine prime numbers up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    # Implementing the Sieve of Eratosthenes
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Precompute the number of prime choices for every n up to max_num
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    # Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
