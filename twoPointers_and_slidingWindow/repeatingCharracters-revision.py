class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = r = maxLen = 0
        hashMap = {}
        while r < n:
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1 
            print(s[r])
            

            # Shriking...
            while hashMap[r] > 1:
                hashMap[l] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen
    
string = 'abcabcbb'
sol = Solution()
res = sol.lengthOfLongestSubstring("abcabcbb")
