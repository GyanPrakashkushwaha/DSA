from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        prev, cur, ahead = None, head, head.next

        while ahead:
            cur.next = prev
            prev = cur
            cur = ahead
            ahead = ahead.next

        return cur
    
    
def buildLL(L):
    root = ListNode(L[0])
    cur = root
    for num in L[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    
    return root

if __name__== '__main__':
    head = [1,2,3,4,5]
    l1LL = buildLL(head)
    
    res = Solution().reverseList(l1LL)
    print(res)
