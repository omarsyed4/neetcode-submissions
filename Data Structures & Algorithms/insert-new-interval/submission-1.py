class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        # compare the newInt
        for i in range(len(intervals)):
            currS, currE = intervals[i]
            s, e = newInterval

            # curr is completely before
            if currE < s:
                res.append(intervals[i])

            # curr is completely after
            elif currS > e:
                res.append(newInterval)
                return res + intervals[i:]

            else:
                # change the new interval
                newInterval = [min(currS, s), max(currE, e)]

        res.append(newInterval)
        
        return res
