def knapsack_bottom_up(wt, val, cap, n):
    # Create a DP table with dimensions (n+1) x (cap+1)
    dp = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]

    # Fill the DP table iteratively
    for i in range(1, n + 1):
        for w in range(1, cap + 1):
            if wt[i - 1] <= w:
                include = val[i - 1] + dp[i - 1][w - wt[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][cap]

# https://monicagranbois.com/knapsack-algorithm-visualization/
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
cap = 7
n = len(wt)

print(knapsack_bottom_up(wt, val, cap, n))  


