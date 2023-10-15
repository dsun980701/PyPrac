class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Logic here is that for n number of integers, in an ordered permutation,
        # the indx = k_j / (n-j)! will be the indx to the jth number in that particular
        # kth permutation; with k constantly being updated as k_j+1 = k_j % (n-j)!
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
            
       