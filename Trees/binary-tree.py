from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftSubtree = self.maxDepth(root.left)
        RightSubtree = self.maxDepth(root.right)
        return max(leftSubtree, RightSubtree) + 1

# build tree
root = [3,9,20,None,None,15,7]
tn = TreeNode(3)
tn.left = TreeNode(9)
tn.right = TreeNode(20)
tn.right.left = TreeNode(15)
tn.right.right = TreeNode(7)
sol = Solution()
print(sol.maxDepth(tn))