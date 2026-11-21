class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lower bound of eating speed: minimum possible (1 banana/hour)
        # upper bound of eating speed: maximum pile size
        lb, ub = 1, max(piles)
        k = ub
        while lb <= ub:
            mid = (lb + ub) // 2
            total_hour = 0
            for i in piles:
                # each pile takes ceil(i / mid) hours at speed 'mid'
                total_hour += math.ceil(i / mid)

            # if Koko can finish within h hours at this speed
            if total_hour <= h:
                # this speed is valid, store it
                k = mid
                # trying to find a smaller valid speed
                ub = mid - 1
            else:
                # else if total_hour > h, this speed is too slow, incrementing the speed
                lb = mid + 1

        return k