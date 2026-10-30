class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # dfs

        # If we've already seen the cell return 0. 
        # If the cell is water return 1.
        # If the cell is out of range, return 1. 

        # If the cell is just more island 
        # Run DFS on the surrounding. 

        rows = len(grid)
        cols = len(grid[0])

        seen = set()
        res = 0

        def dfs(r,c):

            nonlocal res

            if (r,c) in seen:
                return
            
            if r < 0 or c < 0 or r >= rows or c >= cols:
                res += 1
                return

            if grid[r][c] == 0:
                res += 1
                return

            seen.add((r, c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    dfs(r, c)

        return res



