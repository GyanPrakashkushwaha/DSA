from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        self.heights = []
        self.dfs(root, 1)
        print(self.heights)
        diff = max(self.heights) - min(self.heights)
        return True if diff <= 1 else False

    def dfs(self, root, level):
        if not root: return
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
        self.heights.append(level)
        
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution().isBalanced(tree))