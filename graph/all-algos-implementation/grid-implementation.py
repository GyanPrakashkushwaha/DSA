
from collections import deque


def bfsGrid(grid):
    
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]
    directions = [(-1,0), (1,0), (0,1), (0,-1)] # UP DOWN RIGHT LEFT
    
    result = []
    def bfs(r,c):
        queue = deque([(r,c)])
        visited[r][c] = 1
        while queue:
            r, c = queue.popleft()
            result.append((r,c))

            for dr, dc in directions:
                nr, nc = r+dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 1: # Assuming the nodes present are represented by 1 in a cell.
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
    
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1 and not visited[r][c]:
                bfs(r,c)
    
    return result


def dfsGrid(grid):
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]
    directions = [(-1,0), (1,0), (0,1), (0,-1)] # UP DOWN RIGHT LEFT
    
    result = []
    def dfs(r,c):
        visited[r][c] = 1
        result.append((r,c))
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 1: # Assuming the nodes present are represented by 1 in a cell.
                dfs(nr, nc)
                
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r,c)
                
    return result
    
