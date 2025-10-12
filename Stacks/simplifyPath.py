class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        
        for c in path + "/":
            if c == '/':
                if cur == '..':
                    if stack: stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(cur)  
                cur = ""
            else:
                cur += c
        
        ans = ""
        for c in stack:
            ans += '/'+c
        
        return '/' if not stack else ans 
    
Solution().simplifyPath('/.../tbku/../code/google/../dsa/./')