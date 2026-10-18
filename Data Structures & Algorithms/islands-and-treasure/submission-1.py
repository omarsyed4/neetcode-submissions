class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        

        while q:
            r,c = q.popleft()

            for dr, dc in [(0,1), (0,-1), (-1,0), (1,0)]:
                nr, nc = r + dr, c + dc

                if nr >= rows or nc >= cols or nc < 0 or nr < 0:
                    continue
                
                if grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1

                q.append((nr,nc))
                
