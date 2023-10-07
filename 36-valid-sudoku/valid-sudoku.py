class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First answer
        '''
        column = [collections.defaultdict(int) for _ in range(9)]
        cube =[[collections.defaultdict(int) for _ in range(3)] for _ in range(3)] 
        r = 0
        while r < 9:
            row = collections.defaultdict(int)
            c = 0
            while c < 9:
                num = board[r][c]
                if num.isnumeric():
                    row[num] += 1
                    column[c][num] += 1
                    cube[r//3][c//3][num] += 1
                    if row[num] > 1 or column[c][num] > 1 or cube[r//3][c//3][num] > 1:
                        return False
                c += 1
            r += 1
        return True
        '''
        # Approach using set
        seen = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if (i, num) in seen or (num, j) in seen or (i//3, j//3, num) in seen:
                        return False
                    seen.add((i, num))
                    seen.add((num, j))
                    seen.add((i//3, j//3, num))
        return True
                    
                    