from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        for k in range(len(nums)-3):
            # if k > 0 and nums[k-1] == nums[k]: continue
            for l in range(k+1, len(nums)-2):
                # if l > k+1 and nums[l-1] == nums[l]: continue
                i, j = l+1, len(nums)-1
                while i < j:
                    total = nums[k] + nums[l] + nums[i] + nums[j]
                    if total == target:
                        res.append([nums[k], nums[l], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
                    elif total < target:
                        i += 1
                    else:
                        j -= 1

        return res
                    

    
Solution().fourSum([1,0,-1,0,-2,2], 0)