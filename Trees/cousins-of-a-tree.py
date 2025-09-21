import collections

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        if not root: return False
        
        q = collections.deque([root])
        while q:
            size = len(q)
            c = 0
            for _ in range(size):
                node = q.popleft()
                if node.val == x: c += 1
                if node.val == y: c += 1
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            if c == 2: return True
        
        return False

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(3)

sol = Solution()
res = sol.isCousins(root, 3, 4)
print(res)