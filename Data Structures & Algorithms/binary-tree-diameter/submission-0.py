# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Solution.d = 0
        def height(root):
            if not root:
                return 0
            lheight = height(root.left)
            rheight = height(root.right)
            Solution.d = max(Solution.d, lheight + rheight)
            return 1 + max(lheight, rheight)
        
        height(root)
        return Solution.d