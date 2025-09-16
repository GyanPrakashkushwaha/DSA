class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0]*m for _ in range(n)]
        
        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < m and grid[r][c] == '1' and not visited[r][c]):
                return
            visited[r][c] = 1
            dfs(r+1, c) # UP
            dfs(r-1, c) # DOWN
            dfs(r, c+1) # RIGHT
            dfs(r, c-1) # LEFT
        
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i,j)
                    islands += 1
        
        return islands
