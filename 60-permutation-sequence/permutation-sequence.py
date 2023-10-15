class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [f"{n}" for n in range(1,n+1)]
        ans = ''
        factor = math.factorial(n-1)
        k -= 1
        while k > 0 and n > 0:
            indx = int(k // factor)
            ans += nums[indx]
            nums.pop(indx)
            k = k % factor
            factor /= n - 1
            n -= 1
        ans += ''.join(nums)
        return ans
            
       