# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        Solution.count = 1
        def DFS(root, maxnode):
            if not root:
                return
            if root.val >= maxnode.val:
                Solution.count += 1
                maxnode = root
                
            DFS(root.left, maxnode)
            DFS(root.right, maxnode)
        
        DFS(root.left, root)
        DFS(root.right, root)
        return Solution.count
