class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        summ = 0
        minn = 999999999
        start = 0
        for num in nums:
            summ += num
            count += 1
            if summ >= target:
                while summ >= target:
                    count -= 1
                    summ -= nums[start]
                    start += 1
                if minn > count:
                    minn = count
        if minn == 999999999:
            return 0
        return minn + 1
            
