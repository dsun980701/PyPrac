class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        r_max = len(grid) - 1
        c_max = len(grid[0]) - 1
        memo = {}
        def minPath(r, c):
            #Base Case
            if r == r_max and c == c_max:
                return grid[r][c]
            # Check Memo
            if (r,c) in memo:
                return memo[(r,c)]
            a = 9999999
            b = 9999999
            # Problem Reduction
            if r + 1 <= r_max:
                a = minPath(r+1, c)
            if c + 1 <= c_max:
                b = minPath(r, c+1)
            if a > b:
                memo[(r,c)] = b + grid[r][c]
                return b + grid[r][c]
            else:
                memo[(r,c)] = a + grid[r][c]
                return a + grid[r][c]
        return minPath(0,0)