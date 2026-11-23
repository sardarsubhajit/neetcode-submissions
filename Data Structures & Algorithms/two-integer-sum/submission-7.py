class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i
        return []