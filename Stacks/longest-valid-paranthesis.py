class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        st = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    longest = max(longest, i - st[-1])
        
        return longest
    
Solution().longestValidParentheses(s = ")()())")