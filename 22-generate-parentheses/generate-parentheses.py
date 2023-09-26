class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def next_move(n_op, n_cl,curr = ''):
            if n_cl == 0:
                result.add(curr)
                return
            if curr:
                if n_cl > n_op:
                    next_move(n_op, n_cl-1, curr + ')')
                if n_op:
                    next_move(n_op-1, n_cl, curr+'(')
            else:
                next_move(n_op - 1, n_cl, '(')
            
        result = set()
        next_move(n,n)
        return list(result)

        

        