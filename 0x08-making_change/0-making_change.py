#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Make Change Method
    """
    if total == 0:
        return 0
    coins.sort(reverse=True)
    res = 0
    dif = total
    for coin in coins:
        while dif - coin >= 0:
            res = res + 1
            dif = dif - coin
    if dif > 0:
        return -1
    return res
