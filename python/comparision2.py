from collections import deque

def bfs_adj_list(adj):
    n = len(adj)
    visited = [0]*n
    queue = deque([0])
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)
        
    return result