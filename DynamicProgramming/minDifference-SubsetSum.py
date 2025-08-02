def minDifference(arr):
    # SubsetSum
    n, target = len(arr), sum(arr)
    dp = [[None for _ in range(target + 1)] for _ in range(n+1)]
    
    def isSubsetSum(arr, n, target):
        # Base Case
        if target == 0:
            return True
        elif n == 0:
            return False
        if dp[n][target] is not None:
            return dp[n][target]
        # Choices
        exclude = isSubsetSum(arr, n-1, target) # exclude
        include = False
        if arr[n-1] <= target:
            include = isSubsetSum(arr, n-1, target - arr[n-1]) # include
        
        dp[n][target] = include or exclude        
        return dp[n][target]

    minDiff = target
    for subSum in range((target//2)+1):
        if isSubsetSum(arr, n, subSum):
            minDiff = min(minDiff, target - (2*subSum))
    
    return minDiff
    
arr = [1, 4]
minDifference(arr)