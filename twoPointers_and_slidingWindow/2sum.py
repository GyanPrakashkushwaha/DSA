class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = list(enumerate(nums))
        
        arr.sort(key = lambda x: x[1])

        l, r = 0, len(nums)-1

        while l <= r:
            if arr[l][1] + arr[r][1] == target:
                return [arr[l][0], arr[l][0]]
            elif arr[l][1] + arr[r][1] < target:
                l += 1
            else:
                r -= 1
        
        return [-1, -1]
    
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        lookup = {}

        for i in range(len(nums)):
            lookup[nums[i]] = i
        
        for i in range(len(nums)):
            complement = nums[i] - target
            if complement in lookup and lookup[complement] != i:
                return [i, lookup[complement]]
        
        return [-1, -1]


nums = [2,7,11,15]
target = 9
Solution().twoSum2(nums, target)