from collections import deque
def orangeRotting(grid):
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]
    
    def bfs(grid, start):
        queue = deque([start])
        visited[start[0]][start[1]] = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Variable for checking....
        while queue:
            r, c = queue.popleft()
            # return logic.....
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
    
    counter = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j]:
                counter += 1
                bfs(grid, (i,j))
    
    return 4 if counter == 1 else -1
    
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangeRotting(grid))
    