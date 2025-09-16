class Node:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None
        
class Solution:
    def countNodes(self, root) -> int:
        def traverse(node):
            if not node:
                return 0
            leftTree = traverse(node.left) 
            rightTree = traverse(node.right) 
            return leftTree + rightTree + 1
        
        return traverse(root)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
sol = Solution()
res = sol.countNodes(root)
print(res)