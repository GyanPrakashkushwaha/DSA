class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]):
        if not nums:
            return None

        mid = len(nums)//2
        
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

# sortedArrayToBST([1..15]) → root = 8
# ├── Left → 4
# │   ├── Left → 2
# │   │   ├── Left → 1
# │   │   └── Right → 3
# │   └── Right → 6
# │       ├── Left → 5
# │       └── Right → 7
# └── Right → 12
#     ├── Left → 10
#     │   ├── Left → 9
#     │   └── Right → 11
#     └── Right → 14
#         ├── Left → 13
#         └── Right → 15

#                 8
#           /            \
#         4               12
#       /   \           /     \
#      2     6        10       14
#     / \   / \      /  \     /  \
#    1   3 5   7    9   11  13   15


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
root = Solution().sortedArrayToBST(nums)


def printTree(root, level=0, prefix="Root: "):
    if not root:
        return
    # Print right subtree first (so it appears on top when rotated)
    printTree(root.right, level + 1, "R--- ")
    # Print current node
    print("     " * level + prefix + str(root.val))
    # Print left subtree
    printTree(root.left, level + 1, "L--- ")

print(printTree(root))