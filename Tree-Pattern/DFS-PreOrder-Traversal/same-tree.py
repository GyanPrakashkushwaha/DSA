# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.preOrder(p, q)
    
    def preOrder(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.preOrder(
            p.left if p.left else None,
            q.left if q.left else None
        ) and self.preOrder(
            p.right if p.right else None,
            q.right if q.right else None
        )
    
tree_node1 = TreeNode(1)
tree_node2 = TreeNode(1)

tree_node1.left = TreeNode(2)
tree_node2.left = TreeNode(2)
tree_node1.right = TreeNode(3)
tree_node2.right = TreeNode(3)

soln = Solution()
print(soln.isSameTree(tree_node1, tree_node2))