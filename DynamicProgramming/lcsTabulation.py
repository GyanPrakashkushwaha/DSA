text1, text2 = 'ace' , 'abcde'
n, m = len(text1), len(text2)

def lcs(text1, text2, n, m):
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    # Initialization
    for i in range(m+1):
        dp[0][i] = 0
    
    for j in range(1,n+1):
        dp[j][0] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                choice1 = dp[i][j-1]
                choice2 = dp[i-1][j]
                dp[i][j] = max(choice1, choice2)
        
    
    return dp[n][m]
    
    # if dp[n][m] != -1:
    #     return dp[n][m]
    # # Based on choice Diagram.
    # if text1[n - 1] == text2[m - 1]:
    #     dp[n][m] = 1 + lcs(text1, text2, n - 1, m - 1)
    #     return dp[n][m]
    # else:
    #     # choice1 & choice2
    #     choice1 = lcs(text1, text2, n, m - 1)
    #     choice2 = lcs(text1, text2, n - 1, m)
    #     dp[n][m] = max(choice1, choice2)
    #     return dp[n][m]


print(lcs(text1, text2, n, m))