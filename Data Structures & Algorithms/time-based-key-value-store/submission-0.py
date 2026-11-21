from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.datastore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.datastore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        lb, ub = 0, len(self.datastore[key]) - 1
        res = ''
        while lb <= ub:
            mid = (lb + ub) // 2
            if self.datastore[key][mid][0] <= timestamp:
                res = self.datastore[key][mid][1]
                lb = mid + 1
            else:
                ub = mid - 1
        
        return res
