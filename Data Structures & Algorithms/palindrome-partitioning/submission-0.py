class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def is_pal(string) -> bool:
            left = 0
            right = len(string) - 1

            while left <= right:
                if string[left] != string[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True

        
        curr = []

        def dfs(i):

            if i == len(s):
                res.append(curr[:])
                return

            for end in range(i + 1, len(s) + 1):
                substring = s[i:end]

                if is_pal(substring):
                    curr.append(substring)
                    dfs(end)
                    curr.pop()

        dfs(0)
        return res


