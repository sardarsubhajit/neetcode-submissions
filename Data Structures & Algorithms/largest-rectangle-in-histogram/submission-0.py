class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # storing pairs: [indx, height]
        # maintains a monotonically increaing stack
        # so that we can keep track of the smallest heights in the histogram
        for i, h in enumerate(heights):     
            start = i
            # when we find a smaller height
            # then remove the larger heights
            # calculate the area they can cover
            # update the left boundary of the curr histogram
            while stack and stack[-1][1] > h:
                indx, height = stack.pop()
                maxArea = max(maxArea, height * (i-indx))
                start = indx
            
            stack.append((start, h))
        
        while stack:
            indx, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights)-indx))
        
        return maxArea