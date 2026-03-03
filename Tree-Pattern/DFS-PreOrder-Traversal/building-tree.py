
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder: return None
        val = postorder[-1]
        root = TreeNode(val)
        index = inorder.index(val)
        root.left = self.buildTree(inorder[:index], postorder[:-1])
        root.right = self.buildTree(inorder[index+1:], postorder[:-1])
        return root
    
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(Solution().buildTree(inorder, postorder))