# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def postorder(root):
            if not root:
                return 0
            
            leftmax = max(postorder(root.left), 0)  # incase leftmax or rightmax is -ve
            rightmax = max(postorder(root.right), 0)

            Solution.res = max(Solution.res, root.val + leftmax + rightmax)   # without split     
            return root.val + max(leftmax, rightmax)    # with split
        
        if not root:
            Solution.res = 0
        else:
            Solution.res = root.val
        postorder(root)
        return Solution.res