import math
class Solution:
    def replaceNonCoprimes(self, nums):
        stack = []
        for num in nums:
            while stack:
                gcd = math.gcd(int(stack[-1]), num)
                if gcd <= 1:
                    break
                num = (stack.pop()*num)//gcd
            stack.append(num)

        return stack

nums = [6,4,3,2,7,6,2]
sol = Solution()
res = sol.replaceNonCoprimes(nums)
print(res)