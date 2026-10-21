class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        res = 0
        s, e = intervals[0]

        for i in range(1,len(intervals)):

            currS, currE = intervals[i]
            print(intervals[i])

            # if no over lap move to the next
            if e <= currS:
                e = currE
                continue

            # if over lap 
            else:
                res +=1
                e = min(e,currE)
        
        return res


# dp approach? like if i store how many removals per spot then i could just return the last index
# ehh not necessary

# i think right now i just keep a running tally instead

'''
s = 1
e = 100

[[1,100],[11,22],[1,11],[2,12]]
           ^ ^


'''