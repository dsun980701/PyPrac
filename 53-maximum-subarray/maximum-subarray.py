class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > answer:
                answer = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return answer
