class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        area = float('-inf')
        while left < right:
            curr_area = min(heights[left], heights[right])*(right-left)
            area = curr_area if area < curr_area else area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return area