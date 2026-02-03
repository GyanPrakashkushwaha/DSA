class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums: return 0
        nums.sort()
        n = len(nums)

        c = 1
        i, j = 0, 1

        while j < n:
            if nums[j-1] == nums[j] - 1:
                c = max(j - i + 1, c)
                j += 1
            else:
                j += 1
                i += 1
        
        return c
    
nums = [1,2,6,7,8]
soln = Solution()
soln.longestConsecutive(nums=nums)