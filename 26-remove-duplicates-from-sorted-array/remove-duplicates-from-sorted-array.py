class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        # Memory Efficient
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
        '''
        # Time Efficient
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        read_iter = 1
        write_iter = 0
        count = 1
        length = len(nums)
        while read_iter < length:
            if nums[read_iter] != nums[write_iter]:
               write_iter += 1
               nums[write_iter] = nums[read_iter]
               read_iter += 1
               count += 1
            else:
                read_iter += 1
        return count
