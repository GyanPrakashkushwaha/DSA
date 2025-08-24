
from collections import deque


def gridBfs(grid):
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for i in range(n)]
    direction = [(-1, 0), (1,0), (0,1), (0,-1)]
    
    result = []
    def bfs(r, c):
        queue = deque([(r,c)])
        visited[r][c] = 1
        
        while queue:
            r, c = queue.popleft()
            result.append((r,c))
            
            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if 0<= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
        
    for r in range(n):
        for c in range(m):
            if not visited[r][c] and grid[r][c] == 1:
                bfs(r,c)
    
    return result
        
        