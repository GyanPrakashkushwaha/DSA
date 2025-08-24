

from collections import deque

def cycleBfs(adj):
    V = len(adj)
    visited = [0]*V
    
    def bfs(node):
        queue = deque([(node,-1)])
        visited[node] = 1
        
        while queue:
            n, p = queue.popleft()
            
            for nei in adj[n]:
                if not visited[nei]:
                    visited[nei] = 1
                    queue.append((nei, n))
                elif nei != p:
                    return True
                
        return False
    
    for i in range(V):
        if not visited[i]:
            if bfs(i):
                return True
    return False