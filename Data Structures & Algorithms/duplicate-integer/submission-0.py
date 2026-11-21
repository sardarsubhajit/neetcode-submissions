class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aux = list()
        for num in nums:
            if num in aux:
                return True
            else:
                aux.append(num)
        return False
        