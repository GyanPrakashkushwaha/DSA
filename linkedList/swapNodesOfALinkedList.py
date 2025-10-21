from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[Node], k: int) -> Optional[Node]:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        
        cur = head
        node1, node2 = None, None
        for i in range(1, size):
            if i == k:
                node1 = cur
            elif size - k+1 == i:
                node2 = cur
                
        if node1 and node2:
            node1.val, node2.val = node2.val, node1.val

        return head

def buildLL(L):
    root = Node(L[0])
    cur = root
    for num in L[1:]:
        cur.next = Node(num)
        cur = cur.next
    return root

if __name__== '__main__':
    L = [1,2,3,4,5]
    head = buildLL(L)
    
    res = Solution().swapNodes(head, 2)
    print(res)