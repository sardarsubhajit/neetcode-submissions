class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height)-1     # setup the left and right pointers
        maxL, maxR = height[l], height[r]   # setup the left and right bottle neck
        waterVol = 0
        while l < r:
            if maxL <= maxR:    # find the min. bottle neck
                l += 1
                maxL = max(maxL, height[l])
                waterVol += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                waterVol += maxR - height[r]
        
        return waterVol