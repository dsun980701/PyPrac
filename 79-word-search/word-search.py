class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_row = len(board)
        max_column = len(board[0])

        def have_word(r,c,word):
            # Base Case
            if word == "":
                return True
            ## Problem Reduction
            #Up direction
            c_w = word[0]
            if r + 1 < max_row and board[r + 1][c] == c_w:
                board[r + 1][c] = ""
                if have_word(r+1,c,word[1:]):
                    return True
                board[r + 1][c] = c_w
            if r - 1 >= 0 and board[r - 1][c] == c_w:
                board[r - 1][c] = ''
                if have_word(r-1,c,word[1:]):
                    return True
                board[r - 1][c] = c_w
            if c + 1 < max_column and board[r][c + 1] == c_w:
                board[r][c + 1] = ''
                if have_word(r,c + 1,word[1:]):
                    return True
                board[r][c + 1] = c_w
            if c - 1 >= 0 and board[r][c - 1] == c_w:
                board[r][c - 1] = ''
                if have_word(r,c-1,word[1:]):
                    return True
                board[r][c - 1] = c_w
            return False

        r = 0
        start = []
        while r < max_row:
            c = 0
            while c < max_column:
                if board[r][c] == word[0]:
                    start.append((r,c))
                c += 1
            r += 1
        for x in start:
            board[x[0]][x[1]] = ''
            if have_word(x[0],x[1],word[1:]):
                return True
            board[x[0]][x[1]] = word[0]
        return False
            