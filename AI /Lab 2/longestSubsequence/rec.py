def lcs_recursive(s1, s2, m, n, count):
    if m == 0 or n == 0:
        return count
    if s1[m - 1] == s2[n - 1]:
        count = lcs_recursive(s1, s2, m - 1, n - 1, count + 1)
    count = max(count, max(lcs_recursive(s1, s2, m, n - 1, 0),
                           lcs_recursive(s1, s2, m - 1, n, 0)))
    return count

s1 = "dabcde"
s2 = "abfce"
print(lcs_recursive(s1, s2, len(s1), len(s2), 0))
    