def edit_distance(S, T):
    n, m = len(S), len(T)
    
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = i  
    for j in range(m + 1):
        dp[0][j] = j  
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:  
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,     # Deletion
                               dp[i][j - 1] + 1,     # Insertion
                               dp[i - 1][j - 1] + 1) # Substitution
    
    return dp[n][m]

S = "kitten"
T = "sitting"
distance = edit_distance(S, T)
print(f"The edit distance between '{S}' and '{T}' is {distance}.")
