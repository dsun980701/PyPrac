class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # No overlap cases
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        
        # Binary Search for insertion start location
        l ,r = 0, len(intervals) - 1
        indx = -1
        while l <= r:
            mid = (l+r) // 2
            if intervals[mid][1] == newInterval[0]:
                indx = mid
                break
            elif intervals[mid][1] < newInterval[0]:
                l = mid + 1
            else: 
                r = mid - 1
        if indx == -1:
            indx = r + 1

        res = intervals[:indx] 
        while indx < len(intervals) and intervals[indx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[indx][0], newInterval[0])
            newInterval[1] = max(intervals[indx][1], newInterval[1])
            indx += 1
        res.append(newInterval)
        #adding remaining elements to the list
        res += intervals[indx:]  
        return res        
        