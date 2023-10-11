class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        row_max, column_max = len(matrix) - 1, len(matrix[0]) - 1
        row_min, column_min = 0, 0
        while column_max >= column_min and row_max >= row_min:
            for i in range(row_min,column_max+1):
                result.append(matrix[row_min][i])
            row_min += 1
            for i in range(row_min,row_max+1):
                result.append(matrix[i][column_max])
            column_max -= 1
            if (row_min <= row_max):
                for i in range(column_max,column_min-1,-1):
                    result.append(matrix[row_max][i])
                row_max -= 1
            if (column_min <= column_max):
                for i in range(row_max,row_min-1,-1):
                    result.append(matrix[i][column_min])
                column_min += 1
        return result
            
            

