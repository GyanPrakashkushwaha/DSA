from collections import defaultdict


def adjDfs(V, edge):
    adj = defaultdict(list)
    for u, v in edge:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [0]*V
    result = []
    def dfs(src):
        visited[src] = 1
        result.append(src)
        for nei in adj[src]:
            if not visited[nei]:
                dfs(nei)
                
    for i in range(V):
        if not visited[i]:
            dfs(i)
        
    return result



def adjDfs(mat):    
    V = len(mat)
    visited = [0]*V
    result = []
    def dfs(src):
        visited[src] = 1
        result.append(src)
        for nei in range(V):
            if not visited[nei] and mat[src][nei] == 1:
                dfs(nei)
                
    for i in range(V):
        if not visited[i]:
            dfs(i)
        
    return result