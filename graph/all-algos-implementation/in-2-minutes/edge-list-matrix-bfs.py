

from collections import defaultdict, deque


def adjBfs(V, edges):
    
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    print("Adjacency List:")
    for k, v in adj.items():
        print(k, ":", v)
    
    visited = [0]*V
    
    result = []
    def bfs(src):
        queue = deque([src])
        visited[src] = 1
        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = 1
                    queue.append(nei)
                    
        
    for i in range(V):
        if not visited[i]:
            bfs(i)
      
    return result

edges = [[0, 1], [6, 0], [2, 4], [2, 3], [3, 4]]
print(adjBfs(7, edges))

# ============== ADJ MATRIX ========================== # 



def adjMatixBfs(mat):
    V = len(mat)
    visited = [0]*V
    
    result = []
    def bfs(src):
        queue = deque([src])
        visited[src] = 1
        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in range(V):
                if not visited[nei] and mat[node][nei] == 1:
                    visited[nei] = 1
                    queue.append(nei)
                    
        
    for i in range(V):
        if not visited[i]:
            bfs(i)
      
    return result
