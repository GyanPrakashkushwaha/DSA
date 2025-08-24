from collections import deque
# BFSSSS


def isCyclic(adj):
    visited = [0] *len(adj)
    
    def bfs(start):
        visited[start] = 1
        queue = deque([(start, -1)])
        
        while queue:
            node, parent = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
        return False
    
    for i in range(len(adj)):
        if not visited[i]:
            if bfs(i):
                return True
    
    return False

def isCyclicDFS(adj):
    visited = [0] *len(adj)
    
    def dfs(start, parent):
        visited[start] = 1
        
        for neighbor in adj[start]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                if dfs(neighbor, start):
                    return True
            elif neighbor != parent:
                return True
            
        return False
    
    for i in range(len(adj)):
        if not visited[i]:
            if dfs(i, -1):
                return True
            
    return False