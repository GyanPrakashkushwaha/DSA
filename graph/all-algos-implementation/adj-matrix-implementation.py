import collections

def bfs(mat, src):
    V = len(mat)
    visited = [0]*V
    queue = collections.deque([src])
    visited[src] = 1
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for nei in range(V):
            if not visited[nei] and mat[node][nei] == 1:
                visited[nei] = 1
                queue.append(nei)
                
    return result

def dfs(mat, src):
    V = len(mat)
    visited = [0]*V
    result = []
    
    def dfsHelper(node):
        visited[node] = 1
        result.append(node)
        
        for nei in range(V):
            if not visited[nei] and mat[node][nei] == 1:
                dfsHelper(nei)
        
    dfsHelper(src)
    return result