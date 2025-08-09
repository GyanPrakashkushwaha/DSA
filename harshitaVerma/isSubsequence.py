# Recursive Solution

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return self.recursiveSoln(len(s), len(t), s, t)

    def recursiveSoln(self, n: int, m: int, s: str, t: str) -> bool:
        if n == 0: # if the matching string becomes empty then the subsequence exsits otherwise not.
            return True
        if m == 0: # Even if the subsequence don't become empty but the original string becomes empty then its not matching.
            return False
        if s[n-1] == t[m-1]:
            return self.recursiveSoln(n-1, m-1, s, t)
        else:
            return self.recursiveSoln(n, m-1, s, t)

        
# Two Pointers approach
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True 
        i = 0
        j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

