class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def help(nums, curr):
            # Base Case
            if not nums:
                result.append(curr)
            i = 0
            n = len(nums) 
            while i < n:
             help(nums[:i] + nums[i+1:] if i != n - 1 else nums[:i] , curr + [nums[i]])
             i += 1
        help(nums, [])
        return result