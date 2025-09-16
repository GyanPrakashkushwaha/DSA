class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev2 = nums[0]                 # dp[i-2]
        prev1 = max(nums[0], nums[1])   # dp[i-1]
        
        for i in range(2, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, curr
        
        return prev1


# Recursion + memo
class Solution:
    def rob(self, nums):
        dp = [-1 for _ in range(len(nums)+1)]
    
        def robber(n):
            if n <= 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            
            # Rob or skip the house.
            rob_curr = nums[n-1] + robber(n-2) # After robbing the current house skip the adjacent house.
            skip = robber(n-1)
            dp[n] = max(rob_curr, skip) 

            return dp[n]

        return robber(len(nums))