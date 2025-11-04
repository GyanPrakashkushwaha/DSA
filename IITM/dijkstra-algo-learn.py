from collections import defaultdict
import heapq

def dijkstra(edges, V, src):
    # Adj List
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))

    # Initialization
    pq = []
    visited = [0]*V
    visited[src] = 1
    dist = [float('inf')]*V
    heapq.heappush(pq, (0, src))
    
    while pq:
        d, node = heapq.heappop(pq)
        if visited[node]: continue
        visited[node] = 1

        for neig, weight in adj[node]:
            if not visited[neig] and dist[neig] > d + weight:
                dist[neig] = weight + d
                heapq.heappush(pq, (dist[neig], neig))
        
    return dist
                
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5)
]
V = 4
src = 0

print(dijkstra(edges, V, src))
