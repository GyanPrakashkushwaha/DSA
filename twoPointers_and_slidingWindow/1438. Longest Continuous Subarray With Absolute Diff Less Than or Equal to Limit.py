from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if limit == 0: return len(nums)
        l, r = 0, 0
        minn, maxx = float("inf"), float("-inf")
        res = 0
        while r < len(nums):
            minn, maxx = min(minn, nums[r]), max(maxx, nums[r])
            while l < len(nums) and (maxx - minn) > limit:
                l += 1
                minn, maxx = min(minn, nums[l]), max(maxx, nums[l])
            res = max(res, r - l + 1)
            r += 1
            
        return res
    
Solution().longestSubarray(nums = [8,2,4,7], limit = 4)