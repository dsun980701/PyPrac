class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        # Memoized Recursion Method
        '''
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
        '''
        # Grid Reduction method
        r_max = len(grid) 
        c_max = len(grid[0]) 
        for r in range(r_max):
            for c in range(c_max):
                if r == 0 and c ==0:
                    continue
                # Edge case of first row
                elif r == 0:
                    grid[r][c] += grid[r][c-1]
                # Edge case of first column
                elif c == 0:
                    grid[r][c] += grid[r-1][c]
                # Normal cell
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[r_max - 1][c_max - 1]
