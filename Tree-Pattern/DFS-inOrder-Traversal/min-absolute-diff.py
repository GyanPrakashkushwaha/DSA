from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min1 = float("inf")
        self.min2 = float("inf")
        self.inOrder(root)
        return self.min2 - self.min1

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.min1 = min(root.val, self.min1)
        self.min2 = max(self.min1, self.min2)
        # if root and root.val < self.min1:
        #     self.min2 = self.min1
        #     self.min1 = root.val
        self.inOrder(root.right)
        
        
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().getMinimumDifference(root))