from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf')-1, float('inf')-1)

    def validate(self, root, lower, upper):
        if not root: return True

        if not (lower < root.val < upper):
            return False
        
        lTree = self.validate(root.left, lower, root.val)
        rTree = self.validate(root.right, root.val, upper)
        if not lTree or not rTree:
            return False

        return lTree and rTree
    
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().validate(root, float("-inf"), float("inf")))