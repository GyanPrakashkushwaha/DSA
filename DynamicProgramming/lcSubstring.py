def longestCommonSubstring(text1, text2, n, m, count=0):
    if n == 0 or m == 0:
        return count
    if dp[n][m] != -1:
        return dp[n][m]
    
    # choice diagram
    count_new = 0
    if text1[n-1] == text2[m-1]:
        count_new = longestCommonSubstring(text1, text2, n-1, m-1, count+1)
    choice1 = longestCommonSubstring(text1, text2, n, m-1, 0)
    choice2 = longestCommonSubstring(text1, text2, n-1, m, 0)
    
    dp[n][m] = max(count, choice1, choice2) 
        
    return dp[n][m]


s1 = "ABCDGH"
s2 = "ACDGHR"
n, m = len(s1), len(s2)
dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
out = longestCommonSubstring(s1, s2, len(s1), len(s2))
print(out)
