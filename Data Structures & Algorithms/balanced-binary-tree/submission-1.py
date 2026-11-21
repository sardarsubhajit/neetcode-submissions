# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:    
        def DFS(root):
            if not root:
                return (True, 0)    # returns [isbalanced, depth of the node]
            lnode = DFS(root.left)
            rnode = DFS(root.right)
            isbalanced = lnode[0] and rnode[0] and abs(lnode[1] - rnode[1]) < 2
            return (isbalanced, 1 + max(lnode[1], rnode[1]))
        
        return DFS(root)[0]
        