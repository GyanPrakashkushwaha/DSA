from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = cur = Node(0)
        rand = {}
        address = {}
        while cur and root:
            cur.next = Node(root.val)
            rand[root.val] = root.random.val if root.random else None
            address[cur.val] = cur
            root = root.next
            cur = cur.next
        
        cur2 = head.next
        for key, value in rand.items():
            if value:
                cur2.random = address[value]
            else:
                cur2.random = None

            cur2 = cur2.next
        
        return head.next

def buildLL(L):
    root = Node(L[0])
    cur = root
    for num in L[1:]:
        cur.next = Node(num)
        cur.random = 
        cur = cur.next
    
    return root

if __name__== '__main__':
    L = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    head = buildLL(L)
    res = Solution().copyRandomList(head)
    print(res)