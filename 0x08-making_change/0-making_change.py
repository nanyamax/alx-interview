#!/usr/bin/python3
"""determine the fewest number of coins
needed to meet a given amount
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    """Initialize an array to store the minimum
    number of coins for each amount"""
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    '''It takes 0 coins to make change for 0'''

    '''Iterate through each coin and update the
    minimum number of coins needed'''
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount],
                             dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1