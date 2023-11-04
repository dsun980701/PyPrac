class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Creat a Histogram, replacing the binary values to heights of consecutive 1's in the same column
        n, m = len(matrix), len(matrix[0])
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == '1':
                    matrix[r][c] = int(matrix[r-1][c]) + 1 if (r > 0) else 1
                else:
                    matrix[r][c] = 0
        # With the histogram, compute the largest area using previous algorithm from LeetCode Num 84
        result = 0
        for row in matrix:
            row = row + [-1]
            stack = []
            for height in row:
                step = 0
                while stack and stack[-1][0] >= height:
                    h, w = stack.pop()
                    step += w
                    result = max(result, step * h)
                stack.append((height, step + 1))
        return result