


def cycleDfs(adj):
    V = len(adj)
    vis = [0]*V
    
    def dfs(node, parent):
        vis[node] = 1
        
        for nei in adj[node]:
            if not vis[nei]:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True
        
        return False
    
    for i in range(V):
        if not vis[i]:
            if dfs(i,-1):
                return True









