# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.treeSubRoot = None
        # Find the subRoot inside root.
        def dfs(root, subRoot):
            if not root: return
            if root == subRoot:
                self.treeSubRoot = root
                return
            dfs(root.left, subRoot)
            dfs(root.right, subRoot)
        dfs(root, subRoot)

        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            l = sameTree(root.left, subRoot.left)
            r = sameTree(root.right, subRoot.right)
            return l and r
        
        return sameTree(self.treeSubRoot, subRoot)
    
tree = TreeNode(3)
tree.left = TreeNode(4)
tree.right = TreeNode(5)
tree.left.right = TreeNode(2)
tree.left.left = TreeNode(1)

tree2 = tree.left
tree2.left = TreeNode(1)
tree2.right = TreeNode(2)

Solution().isSubtree(tree, tree2)