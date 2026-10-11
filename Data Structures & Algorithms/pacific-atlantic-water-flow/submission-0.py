class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []

        P = set()
        A = set()

        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,visited,prev):

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            if (r,c) in visited:
                return

            if heights[r][c] < prev:
                return
            
            visited.add((r,c))
            
            dfs(r,c-1, visited, heights[r][c])
            dfs(r,c+1, visited, heights[r][c])
            dfs(r+1,c, visited, heights[r][c])
            dfs(r-1,c, visited, heights[r][c])

        
        for r in range(rows):
            # Left edge 
            dfs(r, 0, P, heights[r][0]) 

            # right edge 
            dfs(r, cols-1, A, heights[r][cols-1])         


        for c in range(cols):
            # Top 
            dfs(0, c, P, heights[0][c]) 

            # bottom 
            dfs(rows-1, c, A, heights[rows - 1][c])

        return [[r,c] for r,c in P&A]

        