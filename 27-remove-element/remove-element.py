class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        while True:
            try:
                nums.remove(val)
                length -= 1
            except ValueError:
                break
        return length
