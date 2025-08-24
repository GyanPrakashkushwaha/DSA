from collections import deque

def isCyclicBFS(adj):
    V = len(adj)
    visited = [0]*V

    def bfs(src):
        queue = deque([(src,-1)])
        visited[src] = 1
        
        while queue:
            node,parent = queue.popleft()
            
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = 1
                    queue.append((nei,node))
                elif nei != parent:
                    return True
        
        return False
    
    for node in range(V):
        if not visited[node]:
            if bfs(node):
                return True
    
    return False

def isCyclicDFS(adj):
    V = len(adj)
    visited = [0]*V

    def dfs(node,parent):
        visited[node] = 1
    
        for nei in adj[node]:
            if not visited[nei]:
                if dfs(nei,node):
                    return True
            elif nei != parent:
                return True
        
        return False
    
    for node in range(V):
        if not visited[node]:
            if dfs(node, -1):
                return True
    
    return False