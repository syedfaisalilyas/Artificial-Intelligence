def staircase_ways_recursive(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return staircase_ways_recursive(n - 1) + staircase_ways_recursive(n - 2)

def staircase_ways_memo(n):
    def dp(remaining, memo):
        if remaining == 0:
            return 1
        if remaining == 1:
            return 1
        if remaining in memo:
            return memo[remaining]
        
        memo[remaining] = dp(remaining - 1, memo) + dp(remaining - 2, memo)
        return memo[remaining]
    
    memo = {}
    return dp(n, memo)

def staircase_ways_tabulation(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

if __name__ == "__main__":
    n = 5
    print(f"Number of distinct ways to climb {n} stairs (Recursive): {staircase_ways_recursive(n)}")
    print(f"Number of distinct ways to climb {n} stairs (Memoization): {staircase_ways_memo(n)}")
    print(f"Number of distinct ways to climb {n} stairs (Tabulation): {staircase_ways_tabulation(n)}")
