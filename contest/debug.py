
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1]*n
        st = []
        for i in range(n*2):
            idx = i % n
            while st and nums[st[-1]] < nums[idx]:
                res[st.pop()] = nums[idx]
            if i < n: st.append(i)

        return res
    
nums = [1,2,3,4,3]
Solution().nextGreaterElements(nums)