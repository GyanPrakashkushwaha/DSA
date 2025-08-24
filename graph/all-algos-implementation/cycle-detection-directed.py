# cycle detection using kahns algorithm!
import collections


def CycleDetectionkanhsAlgo(V, edge):
    adj = collections.defaultdict(list)
    for u,v in edge:
        adj[u].append(v)
    
    indegree = [0]*V
    for u in range(V):
        for v in adj[u]:
            indegree[v] += 1
    
    queue = collections.deque([])
    for v in range(V):
        if indegree[v] == 0:
            queue.append(v)
    
    result = []
    # NOW BFS
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
                
    if len(result) != V:
        return True
    
    return False


def topoSortAlgoDetectCycle(V, edge):
    adj = collections.defaultdict(list)
    for u, v in edge:
        adj[u].append(v)
    
    stack = []
    visited = [0]*V
    
    def dfs(node):
        visited[node] = 1
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    # Connect components SYSTEM
    for i in range(V):
        if not visited[i]:
            dfs(i)
            
    return stack[::-1]        