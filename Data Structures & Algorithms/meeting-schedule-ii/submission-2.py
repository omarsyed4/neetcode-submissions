"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        s = e = 0
        res = count = 0

        while s < len(intervals):

            if starts[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            res = max(count,res)

        return res