from typing import List

class Solution:
    def longestOnesBruteForce(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxLen = 0
        for i in range(n):
            counter = 0
            for j in range(i, n):
                if nums[j] == 0:
                    counter += 1
                if counter > k:
                    break
                maxLen = max(maxLen, j - i + 1)
                
                
        
        return maxLen

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
sol = Solution()
res = sol.longestOnesBruteForce(nums, k)
print(res)