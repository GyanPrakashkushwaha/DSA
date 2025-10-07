class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for k in range(len(nums)):
            i, j = k +1, n - k-1

            while i < j:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[k], nums[i], nums[j]]) 
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                else:
                    j -= 1
        
        return res
    
print(Solution().threeSum([-1,0,1,2,-1,-4]))