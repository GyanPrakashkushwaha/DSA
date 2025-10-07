class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s-> i
        # t-> j
        # subsequence found-> if len(s) == i+1

        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
        
        return len(s) == i + 1
    
    
s = "abc"
t = "ahbgdc"
soln = Solution()
print(soln.isSubsequence(s, t))