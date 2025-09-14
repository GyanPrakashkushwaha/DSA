from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        uniqueTrips = set()

        for i in range(n):
            a = -nums[i]
            s = set()
            for j in range(i+1, n):
                b = nums[j]
                c = -(a + b)
                if c in s:
                    trip = (a, b, c)
                    uniqueTrips.add(tuple(sorted(trip)))
                s.add(b)

        return [list(trip) for trip in uniqueTrips]

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))