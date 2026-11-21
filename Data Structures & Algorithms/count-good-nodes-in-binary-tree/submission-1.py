# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxnode):
            if not root:
                return 0
            if root.val >= maxnode.val:
                res = 1
                maxnode = root
            else:
                res = 0
            
            res += dfs(root.left, maxnode)
            res += dfs(root.right, maxnode)
            return res
        
        return dfs(root, root)