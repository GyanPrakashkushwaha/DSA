# IMPLEMENT BOTH BFS and DFS

import collections


def bfs(V, edges, src):
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    
    visited = [0]*V
    queue = collections.deque([src])
    visited[src] = 1
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for nei in adj[node]:
            if not visited[nei]:
                visited[nei] = 1
                queue.append(nei)
    return result

def dfs(V, edges, src):
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    
    visited = [0]*V
    
    result = []
    def dfsHelper(node):
        visited[node] = 1
        result.append(node)
        for nei in adj[node]:
            if not visited[nei]:
                dfsHelper(nei)
    
    dfsHelper(src)
    return result
    
    