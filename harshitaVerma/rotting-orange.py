from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Here we have to find out the depth of the graph if all the nodes are connected...... the fresh is node count other than the 0 level's node. and the minute refers to the depth of the connected graph! So basically we have to find out the number of depth!!
        n, m = len(grid), len(grid[0])
        queue = deque()
        nodes = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    nodes += 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        maxDepth = 0
        while queue:
            r, c, level = queue.popleft()
            maxDepth = max(maxDepth, level)

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    nodes -= 1
                    queue.append((nr, nc, level+1))
        
        return maxDepth if nodes == 0 else -1
