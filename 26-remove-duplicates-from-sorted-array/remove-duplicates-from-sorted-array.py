class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = -999999999
        count, i = 0, 0
        while i < len(nums):
            if nums[i] == check:
                nums.remove(nums[i])
            else:
                check = nums[i]
                i += 1
                count += 1
        return count
