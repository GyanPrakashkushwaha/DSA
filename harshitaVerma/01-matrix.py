from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))  # multi-source BFS starting from all 0s
                else:
                    mat[i][j] = -1  # mark unprocessed 1s

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1  # update distance
                    queue.append((nr, nc))

        return mat
