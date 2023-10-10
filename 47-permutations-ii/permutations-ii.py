class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Solution using set. 
        '''
        result = set()
        def help(nums, curr):
            # Base Case
            if not nums:
                result.add(tuple(curr))
            for i in range(len(nums)):
             help(nums[:i] + nums[i+1:], curr + [nums[i]])
        help(nums, [])
        return result
        '''
        # Solution using counter
        n = len(nums)
        nums = collections.Counter(nums)
        result = []
        def help(nums, curr):
            if len(curr) == n:
                result.append(curr.copy())
            for num in nums:
                if nums[num] > 0:
                    
                    nums[num] -= 1
                    # Concatenation of list is not constant time, hence changed
                    # help(nums, curr + [num])
                    curr.append(num)
                    help(nums, curr)
                    nums[num] += 1
                    curr.pop()
        help(nums, [])
        return result

