def coin_sum(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


if __name__ == '__main__':
    print(coin_sum([1, 2, 5, 10, 20, 50, 100, 200], 200))
