# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1, l2):
            dummy = ListNode()
            ptr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    ptr.next = l1
                    l1 = l1.next
                else:
                    ptr.next = l2
                    l2 = l2.next
                ptr = ptr.next
            
            if l1:
                ptr.next = l1
            
            if l2:
                ptr.next = l2
            
            return dummy.next
        
        if not lists:
            return None
            
        n = len(lists)
        for i in range(1, n):
            lists[i] = mergeTwoLists(lists[i-1], lists[i])

        return lists[n-1]