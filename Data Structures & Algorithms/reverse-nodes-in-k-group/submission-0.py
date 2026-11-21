# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr, count = head, 0
        while count < k:
            if not ptr:
                return head
            ptr = ptr.next
            count += 1
        
        prev = self.reverseKGroup(ptr, k)

        ptr = head
        while count > 0:
            n = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = n
            count -= 1            
        return prev