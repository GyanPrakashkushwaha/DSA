# NORMAL TREE TRAVERSAL WON'T WORD.......
## WILL HAVE TO HAVE THE INFORMATION WHETHER THE TREE IS FROM RIGHT OR LEFT TREEE...
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True
        mainRoot = root.val
        def traverse(root):
            if not root:
                return True
            if root.right:
                if root.right.val < root.val and mainRoot:
                    return False
            if root.left:
                if root.left.val > root.val:
                    return False
            
            left = traverse(root.left)
            right = traverse(root.right)
            
            return left and right
        return traverse(root)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
Solution().isValidBST(root)