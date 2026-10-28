class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        curr = []

        def dfs(num):
            if len(curr) == k:
                res.append(curr[:])
                return

            if num == n:
                return

            # Include
            curr.append(num + 1)
            dfs(num + 1)
            curr.pop()

            # Exclude
            dfs(num + 1)

        dfs(0)
        return res
        

            
            


'''
[1,2,3]

# 1
[]
[1]

# 2
[]
[1]
[2]
[1,2]

# 3
[]
[1]
[1,3]
[2]
[2,3]
[3]
[1,2]
'''