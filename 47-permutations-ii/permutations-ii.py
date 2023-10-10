class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Solution using set. 

        result = set()
        def help(nums, curr):
            # Base Case
            if not nums:
                result.add(tuple(curr))
            for i in range(len(nums)):
             help(nums[:i] + nums[i+1:], curr + [nums[i]])
        help(nums, [])
        return result


