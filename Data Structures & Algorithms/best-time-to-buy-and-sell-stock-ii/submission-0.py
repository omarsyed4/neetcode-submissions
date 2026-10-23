class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        res = 0

        for i, p in enumerate(prices):
            if i == 0:
                continue
            yes = prices[i-1]

            if p > yes:
                res += p - yes
        
        return res


'''
[7,1,5,3,6,4]
     ^

minP = 1
res = 0
'''
