# NORMAL TREE TRAVERSAL WON'T WORD.......
## WILL HAVE TO HAVE THE INFORMATION WHETHER THE TREE IS FROM RIGHT OR LEFT TREEE...
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root) -> bool:
        self.prev = None
        return self.inOrder(root)

    def inOrder(self, root):
        if not root: 
            return True
        left =  self.inOrder(root.left)
        
        if self.prev and self.prev >= root.val:
            return False
        self.prev = root.val
        
        right = self.inOrder(root.right)
        return left and right
    
    

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
print(Solution().isValidBST(root))