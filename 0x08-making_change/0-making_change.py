#!/usr/bin/python3
"""
Function to determine the fewest number
"""

def makeChange(coins, total):
    """
    Function to determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    dp = [0] + [float('inf')] * total
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
