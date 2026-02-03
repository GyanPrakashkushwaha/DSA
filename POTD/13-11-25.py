class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        count = ans = i = 0
        
        while i < n:
            if s[i] == '0':
                ans += count
                while i < n and s[i] != '1':
                    i += 1
            count += 1
            i += 1
        return ans
    
print(Solution().maxOperations("1001101"))