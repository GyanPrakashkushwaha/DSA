import math
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        operations = 0
        for _ in range(n):
            for i in range(n-1):
                gcd = math.gcd(nums[i], nums[i+1])
                if gcd == 1:
                    if nums[i] == 1:
                        nums[i+1] = 1
                    else:
                        nums[i] = 1
                    operations += 1
    
        return operations if operations else -1
    
Solution().minOperations([2,6,3,4])
