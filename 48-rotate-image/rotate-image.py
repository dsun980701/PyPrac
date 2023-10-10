class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if len(matrix) < 2:
            return matrix
        n = len(matrix[0])
        #Reversed column of the current matrix, which will be rows of the new matrix
        rev_column = [[] for _ in range(n)]
        r = n - 1
        while r >= 0:
            c = 0
            while c < n:
                rev_column[c].append(matrix[r][c])
                c += 1
            r -= 1
        for i, new_row in enumerate(rev_column):
            matrix[i] = new_row

