
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


idx = -1
def buildTree(preorder):
    global idx
    idx += 1

    if preorder[idx] == -1:
        return None

    root = Node(preorder[idx])
    root.left = buildTree(preorder)
    root.right = buildTree(preorder)
    return root


# Example
preorder = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, -1]
root = buildTree(preorder)


# # Traversal check
# def preorder_traversal(node):
#     if not node:
#         return [-1]
#     return [node.val] + preorder_traversal(node.left) + preorder_traversal(node.right)


# print("Preorder from tree:", preorder_traversal(root))
