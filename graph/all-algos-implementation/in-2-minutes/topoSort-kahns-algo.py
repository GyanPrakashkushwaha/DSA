


from collections import defaultdict, deque
from pydoc import visiblename


def kahns(V, edge):
    adj = defaultdict(list)
    for u, v in edge:
        adj[u].append(v)
    
    indegree = [0]*V
    for i in range(V):
        for v in adj[i]:
            indegree[v] += 1
        
    queue = deque([])
    for node in range(V):
        if indegree[node] == 0:
            queue.append(node)
    
    result = []
    while queue:
        n = queue.popleft()
        result.append(n)
        
        for nei in adj[n]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    if len(result) != V:
        return []
                
    return result