class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []
        nums = []    

        def dfs(curr, remaining):

            if remaining == 0:
                res.append(nums.copy())
                return
            
            if curr >= len(candidates):
                return

            for i in range(curr, len(candidates)):

                if i > curr and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > remaining:
                    break
                
                nums.append(candidates[i])
                dfs(i+1,remaining - candidates[i])
                nums.pop()


                
        dfs(0, target)

        return res
