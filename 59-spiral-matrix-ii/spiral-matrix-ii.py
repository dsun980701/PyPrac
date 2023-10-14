class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
    
        matrix = [[0]*n for _ in range(n)]
        row_max, column_max = n - 1, n - 1
        row_min, column_min = 0, 0
        num = 1
        while column_max >= column_min and row_max >= row_min:
            for i in range(row_min,column_max+1):
                matrix[row_min][i] = num
                num += 1
            row_min += 1
            for i in range(row_min,row_max+1):
                matrix[i][column_max] = num
                num += 1
            column_max -= 1
            if (row_min <= row_max):
                for i in range(column_max,column_min-1,-1):
                    matrix[row_max][i] = num
                    num += 1
                row_max -= 1
            if (column_min <= column_max):
                for i in range(row_max,row_min-1,-1):
                    matrix[i][column_min] = num
                    num += 1
                column_min += 1
        return matrix
            