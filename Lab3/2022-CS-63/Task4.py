def min_coins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, target + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1

coins = [1, 5, 10, 25]
target = 37
result = min_coins(coins, target)

print(f"Minimum coins required: {result}")
