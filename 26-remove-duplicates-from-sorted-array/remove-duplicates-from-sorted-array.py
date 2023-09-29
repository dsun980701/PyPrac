class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = []
        count, i = 0, 0
        while i < len(nums):
            if nums[i] in check:
                nums.remove(nums[i])
            else:
                check.append(nums[i])
                i += 1
                count += 1
        return count
