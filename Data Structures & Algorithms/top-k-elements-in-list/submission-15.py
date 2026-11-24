from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        
        freq_count = dict(Counter(nums))
        return ([item for item, _ in sorted(freq_count.items(), key=lambda x: -x[1])][:k])