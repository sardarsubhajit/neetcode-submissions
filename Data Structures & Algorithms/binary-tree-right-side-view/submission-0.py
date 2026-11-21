# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = list()
        queue.append(root)
        out = []
        while queue:
            qlen = len(queue)
            level = []
            for _ in range(qlen):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level:
                out.append(level[-1])
        
        return out