class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Previous Answer, preserving order
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
        # Time efficient
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                while length > 0 and nums[length - 1] == val:
                    length -= 1
                if length == i:
                    break
                nums[i] = nums[length - 1]
                length -= 1
            i += 1
        return length
