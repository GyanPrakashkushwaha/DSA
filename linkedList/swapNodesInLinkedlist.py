from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[Node], k: int) -> Optional[Node]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        begin, end = (0, 0, 0), (0, 0, 0) # (Node, prev, next)
        prev = None
        cur = head
        for i in range(length):
            if k-1 == i:
                begin = (cur, prev, cur.next)
            if length - k == i:
                end = (cur, prev, cur.next)
            
            prev, cur = cur, cur.next
                
                
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