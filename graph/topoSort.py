from collections import defaultdict, deque
from re import L
from unittest import result

from sqlalchemy import Visitable

def topoSortAlgo(V, edge):
    adj = defaultdict(list)
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
    
    
def khansAlgo(V, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    
    indegree = [0]*V
    for u in range(V):
        for v in adj[u]:
            indegree[v] += 1
    
    queue = deque([])
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)
            
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != V:
        print('GRAPH CONTAINS CYCLE')
        return [] 
    
    return result
    


def topoSortAlgoDAGDetection(V, edge):
    adj = defaultdict(list)
    for u, v in edge:
        adj[u].append(v)
    
    stack = []
    visited = [0] * V   # 0 = unvisited, 1 = visiting, 2 = visited
    is_cycle = [False]  # flag to detect cycle

    def dfs(node):
        if visited[node] == 1:  # Back edge found → cycle
            is_cycle[0] = True
            return
        if visited[node] == 2:  # Already processed
            return

        visited[node] = 1  # mark as visiting
        for neighbor in adj[node]:
            dfs(neighbor)
        visited[node] = 2  # mark as processed
        stack.append(node)

    # Run DFS on all components
    for i in range(V):
        if visited[i] == 0:
            dfs(i)

    if is_cycle[0]:
        raise ValueError("Graph is not a DAG (contains a cycle).")
    
    return stack[::-1]
