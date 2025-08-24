

from collections import defaultdict
import heapq


def dijkstraAlgo(V, edges, src):
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v,w))
    
    pq = []
    vis = [0]*V
    dist = [float('inf')]*V
    dist[src] = 0
    heapq.heappush(pq, (0, src))
    
    while pq:
        d, n = heapq.heappop(pq)
        
        if vis[n]:
            continue
        
        vis[n] = 1
        for nei, wt in adj[n]:
            if dist[nei] > d + wt:
                dist[nei] = d + wt
                heapq.heappush(pq, (dist[nei], nei))
        
    return dist
            
        
    