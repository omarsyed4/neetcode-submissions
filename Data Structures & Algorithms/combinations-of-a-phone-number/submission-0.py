class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        ntl = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }

        res = []
        curr = []


        def dfs(i):
            if i == len(digits):
                res.append("".join(curr))
                return
            
            letters = ntl[digits[i]]

            for l in letters:
                curr.append(l)
                dfs(i + 1)
                curr.pop()
        
        if not digits:
            return []

        dfs(0)
        return res