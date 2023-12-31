class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Two pointers from k-th element moving
        # The key point in this problem is framing the problem
        # Solver has to understand that we are trying to find the maximum
        # score where length is rewarded, but how small min value is within the
        # subarray is penalized. Code itself is self-explanatory
        min_val = nums[k]
        result = min_val
        len_nums = len(nums)
        r, l = k, k
        while l > 0 or r < len_nums - 1:
            if l == 0:
                r += 1
                min_val = min(min_val, nums[r])
            elif r == len_nums - 1:
                l -= 1
                min_val = min(min_val, nums[l])
            elif nums[l - 1] > nums[r + 1]:
                l -= 1
                min_val = min(min_val, nums[l])
            else:
                r += 1
                min_val = min(min_val, nums[r])
            result = max(result, min_val * (r - l + 1))
        return result