# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(h):
            p, c = None, h
            while c:
                n = c.next
                c.next = p
                p = c
                c = n
            return p

        # finding the sweet point (mid node)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # creating two lists
        # first one to the mide of the list
        # second one from the mid of the list but in reverse
        l1, l2 = head, reverse(slow.next)
        slow.next = None

        # merging the lists to get the resultant list
        while l2:
            t1 = l1.next
            t2 = l2.next

            l1.next = l2
            l2.next = t1

            l1 = t1
            l2 = t2