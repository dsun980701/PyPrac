class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_reach = 0
        for i, num in enumerate(nums):
            if i + num >= maximum_reach:
                maximum_reach = i + num
            if maximum_reach >= len(nums) - 1:
                return True
            if i == maximum_reach:
                break
        return False
            
            
