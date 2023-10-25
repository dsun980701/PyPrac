class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_c = set()
        zero_r = set()
        num_row = len(matrix)
        num_col = len(matrix[0])
        row_zero = [0] * num_col
        r = 0
        for r in range(num_row):
            for c in range(num_col):
                if not matrix[r][c]:
                    zero_c.add(c)
                    zero_r.add(r)
        for r in zero_r:
            matrix[r] = row_zero
        for r in set(range(num_row)) - zero_r:
            for c in zero_c:
                matrix[r][c] = 0

        