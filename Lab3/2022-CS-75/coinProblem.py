def minCoinsRequired(N, coins, memo={}):
    if N == 0:
        return 0
    if N < 0:
        return float('inf')
    if N in memo:
        return memo[N]
    min_coins = float('inf')  
    for coin in coins:
        if coin <= N:
            result = minCoinsRequired(N - coin, coins, memo)  
            min_coins = min(min_coins, 1 + result)  
    memo[N] = min_coins
    return min_coins if min_coins != float('inf') else -1  
target_price = 13
denominations = [ 9,6,5,1]
print(minCoinsRequired(target_price, denominations))  