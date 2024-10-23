def knapsack_recursion(values, weights, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    
    if weights[n - 1] <= capacity:
        include_item = values[n - 1] + knapsack_recursion(values, weights, capacity - weights[n - 1], n - 1)
        exclude_item = knapsack_recursion(values, weights, capacity, n - 1)
        return max(include_item, exclude_item)
    else:
        return knapsack_recursion(values, weights, capacity, n - 1)

def knapsack_memo(values, weights, capacity):
    def dp(i, remaining_capacity, memo):
        if i == 0 or remaining_capacity == 0:
            return 0
        
        if (i, remaining_capacity) in memo:
            return memo[(i, remaining_capacity)]
        
        if weights[i - 1] <= remaining_capacity:
            include_item = values[i - 1] + dp(i - 1, remaining_capacity - weights[i - 1], memo)
            exclude_item = dp(i - 1, remaining_capacity, memo)
            memo[(i, remaining_capacity)] = max(include_item, exclude_item)
        else:
            memo[(i, remaining_capacity)] = dp(i - 1, remaining_capacity, memo)
        
        return memo[(i, remaining_capacity)]
    
    memo = {}
    return dp(len(values), capacity, memo)

def knapsack_tabulation(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    print(f"Maximum value achievable (Recursion): {knapsack_recursion(values, weights, capacity, len(values))}")
    print(f"Maximum value achievable (Memoization): {knapsack_memo(values, weights, capacity)}")
    print(f"Maximum value achievable (Tabulation): {knapsack_tabulation(values, weights, capacity)}")
