class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        len_nums = len(nums)
        for i in range(len_nums):
            num = nums[i]
            if num < 1 or num > len_nums:
                nums[i] = len_nums + 1
        for i in range(len_nums):
            num = abs(nums[i])
            if num > len_nums:
                continue
            num -= 1
            if nums[num] > 0:
                nums[num] *= -1
        for i in range(len_nums):
            if nums[i] > 0:
                return i + 1
        return len_nums + 1