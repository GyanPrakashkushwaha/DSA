class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
    
        if not root: return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left

        return root
    
root = Node(1)
root.left = Node(7)
root.right = Node(9)

root.left.left = Node(2)
root.left.right = Node(6)

root.left.right.left = Node(5)
root.left.right.right = Node(11)

root.right.right = Node(9)
root.right.right.right = Node(5)

res = Solution().invertTree(root)