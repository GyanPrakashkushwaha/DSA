class Node:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None
        
class Solution:
    def isSymmetric(self, root) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))

        return isMirror(root.left, root.right) if root else True

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.right = Node(4)
root.left.right.left = Node(8)
root.left.right.right = Node(9)

root.right = Node(2)
root.right.right = Node(3)
root.right.right.right = Node(6)
root.right.right.left = Node(7)
root.right.left = Node(4)
root.right.left.right = Node(8)
root.right.left.left = Node(9)


sol = Solution()
res = sol.isSymmetric(root)
print(res)