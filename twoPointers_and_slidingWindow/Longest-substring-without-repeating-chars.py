from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0
        min_length = float("inf")
        total = 0
        while j < n:
            total += nums[j]
            while i < n and total >= target:
                min_length = min(min_length, j - i + 1)
                total -= nums[i]
                i += 1
            j += 1

        return min_length
    
print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))