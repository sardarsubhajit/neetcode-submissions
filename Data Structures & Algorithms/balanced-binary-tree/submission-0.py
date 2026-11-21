# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            lheight = height(root.left)
            rheight = height(root.right)
            return 1 + max(lheight, rheight)

        def dfs(root):
            if not root:
                return (True, 0)
            
            lnode = dfs(root.left)
            rnode = dfs(root.right)
            isbalanced = lnode[0] and rnode[0] and abs(lnode[1] - rnode[1]) <= 1
            return (isbalanced, 1 + max(lnode[1], rnode[1]))
        
        return dfs(root)[0]

        