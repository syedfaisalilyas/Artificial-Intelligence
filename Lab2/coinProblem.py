def coin_change_recursive(coins, target):
    def dp(remaining):
        if remaining < 0:
            return float('inf')
        if remaining == 0:
            return 0
        
        min_coins = float('inf')
        for coin in coins:
            result = dp(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        
        return min_coins
    
    result = dp(target)
    return result if result != float('inf') else -1

def coin_change_memo(coins, target):
    def dp(remaining, memo):
        if remaining < 0:
            return float('inf')
        if remaining == 0:
            return 0
        if remaining in memo:
            return memo[remaining]
        
        min_coins = float('inf')
        for coin in coins:
            result = dp(remaining - coin, memo)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        
        memo[remaining] = min_coins
        return min_coins
    
    memo = {}
    result = dp(target, memo)
    return result if result != float('inf') else -1

def coin_change_tabulation(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[target] if dp[target] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    target = 11

    print(f"Minimum number of coins needed (Recursive): {coin_change_recursive(coins, target)}")
    print(f"Minimum number of coins needed (Memoization): {coin_change_memo(coins, target)}")
    print(f"Minimum number of coins needed (Tabulation): {coin_change_tabulation(coins, target)}")
