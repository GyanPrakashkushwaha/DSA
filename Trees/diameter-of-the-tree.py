class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        diameter = 0
        def depth(node):
            nonlocal diameter
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            diameter = max(diameter, left + right)
            
            return max(right, left) + 1
        depth(root)
        return diameter

root = Node(1)
root.left = Node(7)
root.right = Node(9)

root.left.left = Node(2)
root.left.right = Node(6)

root.left.right.left = Node(5)
root.left.right.right = Node(11)

root.right.right = Node(9)
root.right.right.right = Node(5)

res = Solution().diameterOfBinaryTree(root)
print(res)

#        1
#       / \
#      7   9
#     / \    \
#    2   6    9
#       / \     \
#      5  11     5
