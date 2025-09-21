# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root) -> None:
        if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            root.left.right = root.right
        root.right = root.left
        root.left = None

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)

Solution().flatten(root)