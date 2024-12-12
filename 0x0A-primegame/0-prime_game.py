#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime number game.

    Args:
        x (int): The number of rounds.
        nums (list):
            List of integers representing the value of n for each round.

    Returns:
        str: Name of the player that won the most rounds ("Maria" or "Ben"),
             or None if there is no winner.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)

    # Step 1: Precompute primes using Sieve of Eratosthenes
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Step 2: Precompute the number of primes up to each number
    primes_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if is_prime[i] else 0)

    # Step 3: Simulate each round and determine the winner
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:  # Odd count of primes means Maria wins
            maria_wins += 1
        else:  # Even count of primes means Ben wins
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
