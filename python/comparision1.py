from collections import deque
from re import S

def bfs_grid(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = [[0]*cols for _ in range(rows)]
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # Down, Up, Right, Left
    
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    
    result = []
    
    while queue:
        r, c = queue.popleft()
        result.append((r, c))
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc))
    
    return result



def dfs_grid(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = [[0]*cols for _ in range(rows)]
    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # Down, Up, Right, Left
    result = []
    
    def dfs(r, c):
        visited[r][c] = 1
        result.append((r,c))
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nr]:
                dfs(nr, nc)
        
    dfs(start[0], start[1])
    return result
