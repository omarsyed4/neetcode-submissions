class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        L = 0
        R = len(matrix) - 1
        idx = 0

        while L <= R:

            mid = L + (R - L) // 2
            currMin = matrix[mid][0] 
            currMax = matrix[mid][-1] 
            
            if currMin > target:
                R = mid - 1
            elif target > currMax:
                L = mid + 1
            else:
                idx = mid 
                break 
        
        L = 0
        R = len(matrix[idx]) - 1

        while L <= R:

            mid = L + (R - L) // 2

            if matrix[idx][mid] < target:
                L = mid + 1
            elif matrix[idx][mid] > target:
                R = mid - 1
            else:
                return True
        
        return False