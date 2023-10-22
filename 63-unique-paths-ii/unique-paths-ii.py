class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Check existence of the obstacelGrid
        if not obstacleGrid:
            return 0 
        # Initialize memo
        memo = {}
        # Find the max row num and col num
        r_max, c_max = len(obstacleGrid)-1, len(obstacleGrid[0])-1
        # No path if obstacle is at the goal
        if obstacleGrid[r_max][c_max] or obstacleGrid[0][0]:
            return 0 
        def path(r,c):
            # Base Case
            if r == r_max and c == c_max:
                return 1
            # Check memo
            if (r,c) in memo:
                return memo[(r,c)]
            num_path = 0
            # Problem reduction
            if r + 1 <= r_max and not obstacleGrid[r+1][c]:
                num_path += path(r+1,c)
            if c + 1 <= c_max and not obstacleGrid[r][c+1]:
                num_path += path(r,c+1)
            memo[(r,c)] = num_path
            return num_path
        return path(0,0)