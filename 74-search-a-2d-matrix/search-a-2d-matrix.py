class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Two binary search: first row, THEN column
        '''
        # Binary search the row which has the target
        r, l = len(matrix)-1, 0
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        row = r
        # Binary Search through the column within the found row to find target
        r, l = len(matrix[0])-1, 0
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        '''
        # One binary search through the entire matrix
        num_row = len(matrix)
        num_col = len(matrix[0])
        l, r = 0, num_row * num_col - 1
        while l <= r:
            mid = (l + r) // 2
            curr = matrix[mid // num_col][mid % num_col]
            if curr == target:
                return True
            elif curr < target:
                l = mid + 1
            else:
                r = mid - 1
        return False