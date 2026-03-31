from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        D1 = Counter(s1)
        found = len(D1)
        i = 0
        while i < len(s2):
            while i < len(s2) and s2[i] in D1:
                D1[s2[i]] -= 1
                if D1[s2[i]] == 0:
                    found -= 1
                if found == 0:
                    return True
                i += 1
            D1 = Counter(s1).copy()
            found = len(D1)
            i += 1
        
        return False
    
Solution().checkInclusion(s1 = "hello", s2 = "ooolleoooleh")