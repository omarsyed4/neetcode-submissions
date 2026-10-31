class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[0] * n for _ in range(m)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == 0 or i == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        

        

        return grid[m-1][n-1]