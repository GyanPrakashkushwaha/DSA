
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode) -> list[list[int]]:
    # Handle the edge case of an empty tree
    if not root:
        return []

    # Use a deque for an efficient queue implementation
    result = []
    q = collections.deque([root])

    while q:
        # Get the number of nodes at the current level
        level_size = len(q)
        current_level_values = []

        # Process all nodes at the current level
        for _ in range(level_size):
            node = q.popleft()
            current_level_values.append(node.val)

            # Enqueue children for the next level
            if node.left:
                q.append(node.left)
            if node.right:
                q.ap   pend(node.right)

        # Add the completed level to the result
        result.append(current_level_values)

    return result

# Example Usage:
# Create a sample tree:
#       3
#      / \
#     9  20
#       /  \
#      15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Perform level order traversal
traversal_output = levelOrder(root)
print(f"Level Order Traversal: {traversal_output}")
# Output: Level Order Traversal: [[3], [9, 20], [15, 7]]
