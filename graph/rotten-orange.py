from collections import deque
def orangeRotting(grid):
    
    def bfs(grid, start):
        n, m = len(grid), len(grid[0])
        visited = [[0]*m for _ in range(n)]
        queue = deque([start])
        visited[start[0]][start[1]] = 1
        
        while queue:
            r, c = queue.popleft()
            if not (0 <= r < n and 0 <= c <= m and not visited[r][c] and grid[r][c]):
                continue
            queue.append(r - 1, c) # UP
            queue.append(r + 1, c) # DOWN
            queue.append(r, c + 1) # RIGHT
            queue.append(r, c - 1) # LEFT
            # return logic.....
            
            
        