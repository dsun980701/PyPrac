class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def help(nums, curr):
            # Base Case
            if not nums:
                result.append(curr)
            for i in range(len(nums)):
             help(nums[:i] + nums[i+1:], curr + [nums[i]])
        help(nums, [])
        return result