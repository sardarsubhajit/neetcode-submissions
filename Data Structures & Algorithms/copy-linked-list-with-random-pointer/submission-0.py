"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_map = {None: None}
        # first creating a copy map of the original list
        # so that copy of every node is available
        ptr = head
        while ptr:
            copy_node = Node(ptr.val)
            copy_map[ptr] = copy_node
            ptr = ptr.next
        
        # next simply adding the next and random pointer to the copy node
        ptr = head
        while ptr:
            copy_node = copy_map[ptr]
            copy_node.next = copy_map[ptr.next]
            copy_node.random = copy_map[ptr.random]
            ptr = ptr.next
        
        return copy_map[head]