class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        res = []

        s,e = intervals[0]

        for i in intervals:

            currS, currE = i

            # if the prev/running int is completely before
            if e < currS:
                res.append([s,e])
                s = currS
                e = currE

                # add the prev int to res
                # update the s and e to the curr int

            # if the prev/running int is overlapped
            # since its alr sorted, only look at the e
            else:
                e = max(e,currE)

                # update the e
                # continue

        res.append([s,e])
        return res

    



