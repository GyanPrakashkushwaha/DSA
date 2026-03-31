from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        need, have = defaultdict(int), defaultdict(int)
        res = ''
        maxLen = float("inf")
        for c in t:
            need[c] = need.get(c, 0) + 1
            have[c] = 0
        
        needC, haveC = len(need), 0
        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in need:
                have[char] += 1
                if have[char] == need[char]:
                    haveC += 1
            
            # Shrinking
            while haveC == needC:
                char = s[l]
                if maxLen > r - l + 1:
                    res = s[l:r+1]
                    maxLen = r - l + 1
                have[char] -= 1
                if char in need:
                    if have[char] < need[char]: haveC -= 1
                l += 1
        
        return res

Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")