class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 2 or n == 3:
            return []
        elif n == 1:
            return [['Q']]

        def next_move(prohibited_moves, n_queen):
            # Base Case
            if n_queen == n:
                result.append([''.join(row[:]) for row in board])
                return
            #Problem reduction
            r, c = n_queen, 0
            while c < n:
                if (r, c) in prohibited_moves:
                    c += 1
                    continue
                pm_copy = prohibited_moves.copy()
                board[r][c] = 'Q'
                # Prohibit same column placements in next rows
                for rr in range(r + 1, n):
                    pm_copy.add((rr, c))
                # Prohibit diagonal
                tmp_r, tmp_c = r + 1, c + 1
                while tmp_r < n and tmp_c < n:
                    pm_copy.add((tmp_r, tmp_c))
                    tmp_r += 1
                    tmp_c += 1
                # Prohibit anti-diagonal
                tmp_r, tmp_c = r + 1, c - 1
                while tmp_r < n and tmp_c >= 0:
                    pm_copy.add((tmp_r, tmp_c))
                    tmp_r += 1
                    tmp_c -= 1
                next_move(pm_copy, n_queen + 1)
                board[r][c] = '.'
                c += 1

        # Initialize board
        board = [['.'] * n for _ in range(n)]
        # Will consist of all valid boards
        result = []
        # Will consist of all invalid move positions in tuple(row,column)
        prohibited_moves = set()
        next_move(prohibited_moves, 0)
        return result
