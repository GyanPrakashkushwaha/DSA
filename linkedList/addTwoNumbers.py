from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        cur = ans
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            val = total%10
            carry = total//10
            cur.next = ListNode(val)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        while carry != 0:
            val = carry%10
            carry = carry//10
            cur.next = ListNode(val)
            cur = cur.next
            
        return ans.next

def buildLL(L):
    root = ListNode(L[0])
    cur = root
    for num in L[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    
    return root

if __name__== '__main__':
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    l1LL = buildLL(l1)
    l2LL = buildLL(l2)
    
    res = Solution().addTwoNumbers(l1LL, l2LL)
    print(res)