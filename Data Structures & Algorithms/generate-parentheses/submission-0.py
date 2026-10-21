class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        curr = []
        res = []
        
        def dfs(openP,closedP):

            if openP == closedP == n:
                res.append("".join(curr))
                return
            
            if openP < n:
                curr.append("(")
                dfs(openP + 1, closedP)
                curr.pop()
            if closedP < openP:
                curr.append(")")
                dfs(openP, closedP+1)
                curr.pop()
            
        dfs(0,0)

        return res
        

