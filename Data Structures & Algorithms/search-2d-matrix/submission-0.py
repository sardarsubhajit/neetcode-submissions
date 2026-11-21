class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lb, ub =  0, (m*n)-1
        while lb <= ub:
            mid = (lb+ub)//2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                lb = mid + 1
            else:
                ub = mid - 1
        
        return False