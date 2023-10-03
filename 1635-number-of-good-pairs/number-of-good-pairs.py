class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # First Answer Using sorting, Memory Efficient
        '''
        len_nums = len(nums)
        pair_num = 0
        if len_nums < 2:
            return pair_num
        nums.sort()
        l, r = 0, 1
        while r < len_nums:
            if nums[r] == nums[l]:
                len_same_numbers = 1
                while r < len_nums and nums[r] == nums[l]:
                   len_same_numbers += 1
                   r += 1
                pair_num += math.comb(len_same_numbers, 2)
                l = r - 1
            else:
                 r += 1
                 l += 1
        return pair_num
        '''
        # Second answer using dict
        a = collections.Counter(nums)
        pair_num = 0
        for val in a.values():
            if val >= 2:
                pair_num += math.comb(val, 2)
        return pair_num

            

