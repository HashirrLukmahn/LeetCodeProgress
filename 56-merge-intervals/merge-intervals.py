class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        intervals.sort()
        result = [intervals[0]]


        for i in range(1,n):
            if result[-1][1] >= intervals[i][0]:
                newInterval = [min(result[-1][0],intervals[i][0]),max(result[-1][1], intervals[i][1])]
                result[-1] = newInterval
            else:
                result.append(intervals[i])


        return result


        


