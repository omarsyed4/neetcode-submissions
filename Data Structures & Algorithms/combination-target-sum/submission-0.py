class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        path = []

        def dfs(start, remaining):

            if remaining == 0:
                res.append(path.copy())
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):

                # Explore this option first. 
                path.append(nums[i])

                # Recursive call
                dfs(i, remaining - nums[i])

                # clean the slate
                path.pop()

        dfs(0, target)

        return res
            




