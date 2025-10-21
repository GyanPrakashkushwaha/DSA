from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[Node]) -> Optional[Node]:
        dummy = Node(0, head)
        prev, cur = dummy, head
        
        while cur and cur.next:
            first = cur
            second = cur.next

            # swap
            prev.next = second
            first.next = second.next
            second.next = first

            # move pointers
            prev = first
            cur = first.next

        return dummy.next

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
    
    res = Solution().swapPairs(head)
    print(res)