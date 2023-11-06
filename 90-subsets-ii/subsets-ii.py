class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Answer using collections
        # Sorting, then recursion also works, but since sorting is O(nlogn), and 
        # collections is O(n), I used collections
        len_nums = len(nums)
        result = []
        result.append(tuple(nums))
        nums = collections.Counter(nums)
        
        def subset(curr):
            # Base Case
            if len(curr) == len_nums:
                return
            # Append the curr
            result.append(tuple(curr))
            # 
            for key, val in nums.items():
                if val == 0 or (curr and curr[-1] > key):
                    continue
                nums[key] -= 1
                curr.append(key)
                subset(curr)
                nums[key] += 1
                curr.pop()
        subset([])
        return result
