from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.k = k
        nums = [i+1 for i in range(n)]
        self.count = 1
        self.res = []
        def backtrack(start):
            if start == n-1:
                if self.count == self.k:
                    self.res = nums.copy()
                    return
                self.count += 1
                return
            
            for i in range(start, n):
                if self.res:
                    break
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return "".join([str(i) for i in self.res])


# find next permutation of [1,2,3]
# nums = [1,2,3]
print(Solution().getPermutation(n = 3, k = 3))