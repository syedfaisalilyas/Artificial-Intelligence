def longest_common_substring_recursion(s1, s2, i, j):
    if i == 0 or j == 0:
        return 0
    
    if s1[i - 1] == s2[j - 1]:
        return longest_common_substring_recursion(s1, s2, i - 1, j - 1) + 1
    else:
        return 0

def longest_common_substring_memo(s1, s2):
    def dp(i, j, memo):
        if i == 0 or j == 0:
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if s1[i - 1] == s2[j - 1]:
            memo[(i, j)] = dp(i - 1, j - 1, memo) + 1
        else:
            memo[(i, j)] = 0
        
        return memo[(i, j)]
    
    len1 = len(s1)
    len2 = len(s2)
    memo = {}
    max_length = 0
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            max_length = max(max_length, dp(i, j, memo))
    
    return max_length

def longest_common_substring_tabulation(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    LCS = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    max_length = 0
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
                max_length = max(max_length, LCS[i][j])
            else:
                LCS[i][j] = 0
    
    return max_length


if __name__ == "__main__":
    s1 = "abcde"
    s2 = "abfce"
    
    max_length_recursion = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            max_length_recursion = max(max_length_recursion, longest_common_substring_recursion(s1, s2, i, j))
    
    print(f"Length of Longest Common Substring (Recursion): {max_length_recursion}")
    print(f"Length of Longest Common Substring (Memoization): {longest_common_substring_memo(s1, s2)}")
    print(f"Length of Longest Common Substring (Tabulation): {longest_common_substring_tabulation(s1, s2)}")
