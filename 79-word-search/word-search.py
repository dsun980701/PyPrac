class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_row = len(board)
        max_column = len(board[0])
        word_len = len(word)

        # Function for backtrack
        def have_word(r,c,word_indx):
            # Base Case
            if word_indx == word_len:
                return True
            ## Problem Reduction
            c_w = word[word_indx]
            if r + 1 < max_row and board[r + 1][c] == c_w:
                board[r + 1][c] = ""
                if have_word(r+1,c, word_indx + 1):
                    return True
                board[r + 1][c] = c_w
            if r - 1 >= 0 and board[r - 1][c] == c_w:
                board[r - 1][c] = ''
                if have_word(r-1,c, word_indx + 1):
                    return True
                board[r - 1][c] = c_w
            if c + 1 < max_column and board[r][c + 1] == c_w:
                board[r][c + 1] = ''
                if have_word(r,c + 1, word_indx + 1):
                    return True
                board[r][c + 1] = c_w
            if c - 1 >= 0 and board[r][c - 1] == c_w:
                board[r][c - 1] = ''
                if have_word(r,c-1, word_indx + 1):
                    return True
                board[r][c - 1] = c_w
            return False

        # Find all the starting locations
        r = 0
        start = []
        while r < max_row:
            c = 0
            while c < max_column:
                if board[r][c] == word[0]:
                    start.append((r,c))
                c += 1
            r += 1
        # Use all the starting locations
        for x in start:
            board[x[0]][x[1]] = ''
            # Recursion start
            if have_word(x[0],x[1],1):
                return True
            board[x[0]][x[1]] = word[0]
        return False
            