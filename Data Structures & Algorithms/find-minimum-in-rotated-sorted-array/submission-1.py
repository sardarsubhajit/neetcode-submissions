class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb, ub = 0, len(nums)-1
        minimum = float('inf')

        while lb <= ub:
            # if the current part is already sorted in ascending order
            if nums[lb] <= nums[ub]:
                minimum = min(minimum, nums[lb])
                break
            
            mid = (lb+ub)//2
            minimum = min(minimum, nums[mid])
            # if left part is sorted
            # then min element must be in right part
            if nums[lb] <= nums[mid]:
                lb = mid + 1
            # if right part is sorted
            # then min element must be in left part
            else:
                ub = mid - 1
        
        return minimum