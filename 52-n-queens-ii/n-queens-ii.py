class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 2 or n == 3:
            return 0
        elif n == 1:
            return 1

        def next_move(prohibited_moves, n_queen):
            nonlocal RESULT
            # Base Case
            if n_queen == n:
                RESULT += 1
                return
                
            #Problem reduction
            r, c = n_queen, 0
            while c < n:
                if (r, c) in prohibited_moves:
                    c += 1
                    continue
                pm_copy = prohibited_moves.copy()
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
                c += 1
        # Will consist of all valid board num
        RESULT = 0
        # Will consist of all invalid move positions in tuple(row,column)
        prohibited_moves = set()
        next_move(prohibited_moves, 0)
        return RESULT

        # HAHA answer
        '''
        res = [0,1,0,0,2,10,4,40,92,352]
        return res[n]
        '''