class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Previous Answer
        '''
        if k == 1:
            return nums
        #left and right pointer
        l, r = 0, k - 1
        maxi = max(nums[l:k])
        result = [maxi,]
        r += 1
        while r < len(nums):
            if nums[l] == maxi:
                l += 1
                maxi = max(nums[l:r])
            else: 
                l += 1
            if nums[r] > maxi:
                maxi = nums[r]
            result.append(maxi)
            r += 1
        return result
        '''
        # Solution using double ended queue
        q = collections.deque()
        result = []
        l, r = 0, 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if r >= k - 1 :
                l += 1
                result.append(nums[q[0]])
            r += 1
        return result




