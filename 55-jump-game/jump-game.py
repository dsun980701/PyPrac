class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_reach = 0
        for i, num in enumerate(nums):
            if i + num >= maximum_reach:
                maximum_reach = i + num
            if i == maximum_reach:
                break
        return maximum_reach >= len(nums) - 1
            
            
