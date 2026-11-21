class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lb, ub = 1, max(piles)
        k = ub
        while lb <= ub:
            mid = (lb+ub)//2
            total_hour = 0
            for i in piles:
                total_hour += math.ceil(i/mid)
            
            if total_hour <= h:
                k = mid
                ub = mid - 1
            else:
                lb = mid + 1                
        
        return k
