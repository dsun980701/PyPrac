class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        n = len(intervals)
        if n < 2:
            return intervals
        result = []
        l, r = 0, 0
        while l < n:
            maxi = intervals[l][1]
            while r + 1 < n and intervals[r+1][0] <= maxi:
                maxi = max(maxi, intervals[r+1][1])
                r += 1
            result.append((intervals[l][0], maxi))
            l = r + 1
        return result
            

