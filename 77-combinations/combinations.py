class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Make empty list to store result
        result = []
        # Recursive function
        def permutate(k, curr):
            # Base Case
            if k == 0:
                result.append(curr)
                return
            # Problem Reduction
            # On the initial stack of the recursion, curr is empty, so there cannot be a reference point to start the combination. Hence, since al of our ranges begin with 1
            if not curr:
                i = 1
            # In other cases, reference the previously added num
            else:
                i = curr[-1] + 1
            # Reduce the problem
            for j in range(i,n+1):
                permutate(k-1, curr + [j])
        permutate(k,[])
        return result