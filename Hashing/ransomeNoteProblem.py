from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        print(st1 & st2)
        if st1 & st2 == st1:
            return True
        return False

ransomNote = "aa"
magazine = "aab"

print(Solution().canConstruct(ransomNote, magazine))