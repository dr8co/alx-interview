#!/usr/bin/python3
"""
A function that determines the fewest number of coins needed to meet a given
amount total
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        if coin <= total:
            num_coins += total // coin
            total = total % coin
    if total != 0:
        return -1
    return num_coins
