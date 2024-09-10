from math import gcd

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        gcds = []
        l = head
        r = l
        while l.next != None:
            r = l.next 
            gcds.append(gcd(l.val ,r.val))
            l = r 
            
        cur = head 
        for val in gcds: 
            node = ListNode(val)
            old_next = cur.next
            cur.next = node 
            node.next = old_next 
            cur = cur.next.next
            
            
            
        return head 
    
            