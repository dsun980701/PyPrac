class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {} # key:val -> tuple(x,y,moves):num paths
        # Zero-index the m and n values
        m -= 1 
        n -= 1
        def findPaths(x,y,moves):
            # Base Case
            if x == m and y == n:
                return 1
            # Memoize
            if (x,y,moves) in memo:
                return memo[(x,y,moves)]
            # Find path
            paths = 0
            if x < m:
                paths += findPaths(x+1,y,moves+1)
            if y < n:
                paths += findPaths(x, y+1, moves+1)
            memo[(x,y,moves)] = paths
            return paths
        return findPaths(0,0,0)