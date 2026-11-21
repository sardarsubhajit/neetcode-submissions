class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums)-1

        while lb <= ub:
            mid = (lb + ub) // 2
            if nums[mid] == target:
                return mid
            
            if nums[lb] <= nums[mid]:
                if nums[lb] <= target <= nums[mid]:
                    ub = mid - 1
                else:
                    lb = mid + 1
            else:
                if nums[mid] <= target <= nums[ub]:
                    lb = mid + 1
                else:
                    ub = mid - 1
        
        return -1