class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.next = None
        
class Solution:
    def connect(self, root):
        if not root: return None
        L, R, N = root.left, root.right, root.next
        if L: 
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)


sol = Solution()
res = sol.connect(root)
print(res)



class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        
        if not root:
            return None
        cur  = root
        next = root.left

        while cur.left :
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next
                next = cur.left