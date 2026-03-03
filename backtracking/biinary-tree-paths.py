from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        path = []
        self.res = ''

        def dfs(root):
            if not root: return
            path.append(root.val)
            if not root.left and not root.right:
                string = "".join([chr(num + 97) for num in path])
                if self.res > string:
                    self.res = string
            dfs(root.left)
            dfs(root.right)
            path.pop()
        dfs(root)

        return self.res
        
# --- Level 0 (Root) ---
root = TreeNode(0)

# --- Level 1 ---
root.left = TreeNode(1)
root.right = TreeNode(2)

# --- Level 2 ---
root.left.left = TreeNode(3)

root.right.left = TreeNode(4)
root.right.right = TreeNode(4)
root.right.left = TreeNode(3)

print(Solution().smallestFromLeaf(root))