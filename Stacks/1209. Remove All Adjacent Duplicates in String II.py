class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, count]
        for c in s:
            if stack and stack[-1][0] == c and stack[-1][1] == k-1:
                while stack[-1][0] == c:
                    stack[-1][1] -= 1
                    if stack[-1][1] == 0:
                        stack.pop()
            else:
                if stack and stack[-1][0] == c:
                    stack[-1][1] += 1
                else:
                    stack.append([c, 1])
                
        res = ''
        for char, _ in stack:
            res += char
        
        return res

    
s = "deeedbbcccbdaa"
k = 3
sol = Solution()
res = sol.removeDuplicates(s, k)
print(res)