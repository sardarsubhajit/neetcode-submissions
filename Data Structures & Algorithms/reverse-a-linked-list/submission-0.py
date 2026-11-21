# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p, c, n = None, head, head.next

        while c:
            c.next = p
            p = c
            c = n
            n = n.next if n else None
        
        head = p
        return head