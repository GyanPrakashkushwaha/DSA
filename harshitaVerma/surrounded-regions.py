class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(r, c):
            board[r][c] = 'T'
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == 'O':
                    dfs(nr, nc)

        for r in range(row):
            for c in range(col):
                if ((r in [0, row-1] or c in [0, col-1]) and 
                    board[r][c] == 'O'):
                    dfs(r, c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'T':
                    board[r][c] = 'O'