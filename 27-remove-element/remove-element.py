class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # PreviousAnswer
        '''
        length = len(nums)
        while True:
            try:
                nums.remove(val)
                length -= 1
            except ValueError:
                break
        return length
        '''
        # TimeEfficient
        l, r =0, 0
        len_nums = len(nums)
        while r < len_nums:
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
   
