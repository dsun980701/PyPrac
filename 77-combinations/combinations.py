class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def permutate(k, curr):
            # Base Case
            if k == 0:
                result.append(curr)
                return
            # Problem Reduction
            if not curr:
                i = 1
            else:
                i = curr[-1] + 1
            for j in range(i,n+1):
                permutate(k-1, curr + [j])
        permutate(k,[])
        return result