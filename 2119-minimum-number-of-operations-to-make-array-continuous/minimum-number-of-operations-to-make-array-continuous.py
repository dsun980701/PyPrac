class Solution:
    def minOperations(self, nums: List[int]) -> int:
        orignial_length = len(nums) 
        nums = sorted(set(nums))
        mini = orignial_length
        r = 0
        for l in range(len(nums)):
            while r < len(nums) and nums[r] < nums[l] + orignial_length:
                r += 1
            mini = min(mini, orignial_length - (r - l))
        return mini