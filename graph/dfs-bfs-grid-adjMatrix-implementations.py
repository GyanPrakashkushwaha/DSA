# BFS Adj Matrix Implementation
from collections import deque
def bfsAdj(adj, start):
    n = len(adj)
    visited = [0]*n
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        node = queue.popleft()
        # Do use counter , result, anything you want!!!!
        for neighbor in adj[node]:
            if adj[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)

# BFS GRID                
def bfsGrid(grid, start):
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # UP, DOWN, RIGHT, LEFT
    
    while queue:
        r, c = queue.popleft() # fetch one node.
        # Do whatever you want!!!!
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 1:
                visited[nr][nc] = 1
                queue.append((nr, nc))

# DFS Adj Matrix implementation
def dfsAdj(adj, start):
    visited = [0]*len(adj)
    
    def dfs(node):
        visited[node] = 1
        # Do whatever you want IN the result.......
        for neighbor in adj[node]:
            if adj[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    dfs(start)
    
# DFS GRID
def dfsgrid(grid, start):
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    def dfs(r, c): # the (r,c) forms a node!
        visited[r][c] = 1
        # line for results
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and not visited[nr][nc]:
                dfs(nr, nc)

    dfs(start[0], start[1])
    
    
    
# DFS and BFS GRID with directions

from collections import deque
# BFS GRID                
from collections import deque

def bfsGrid(grid, start):
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]
    queue = deque([start])

    while queue:
        r, c = queue.popleft()
        # base case: skip invalid, visited, or blocked cells
        if r < 0 or r >= n or c < 0 or c >= m or visited[r][c] or grid[r][c] != 1:
            continue
        visited[r][c] = 1

        # enqueue neighbors
        queue.append((r-1, c))  # UP
        queue.append((r+1, c))  # DOWN
        queue.append((r, c-1))  # LEFT
        queue.append((r, c+1))  # RIGHT



# DFS GRID
def dfsgrid(grid, start):
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]

    def dfs(r, c):
        # base case: out of bounds, already visited, or invalid cell
        if r < 0 or r >= n or c < 0 or c >= m or visited[r][c] or grid[r][c] != 1:
            return
        visited[r][c] = 1
        dfs(r-1, c)  # UP
        dfs(r+1, c)  # DOWN
        dfs(r, c-1)  # LEFT
        dfs(r, c+1)  # RIGHT

    dfs(*start)

    