class Node:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None
        
    
def height(node):
    if not node:
        return 0
    leftHeight = height(node.left)
    rightHeight = height(node.right)
    return max(leftHeight, rightHeight) + 1

root = Node(3)
# root.left = Node(9)
# root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)

print(height(root))