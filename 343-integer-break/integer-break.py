class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        threes = n // 3
        r = n % 3
        if r == 1:
            threes -= 1
            r += 3
        elif r == 0:
            r = 1
        return (r) * 3**threes 
