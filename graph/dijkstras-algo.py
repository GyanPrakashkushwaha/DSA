from multiprocessing import heap
import sys
import heapq
from collections import defaultdict

def dijkstra(V, edges, src):
    # Create adjacency list
    adj = constructAdj(edges, V)
    
    dist = [sys.maxsize] * V
    visited = [0] * V
    pq = [(0, src)] # Min-heap priority queue
    dist[src] = 0

    while pq:
        d, node = heapq.heappop(pq)

        if visited[node]:
            continue
        visited[node] = 1  # mark node finalized here

        for neighbor, weight in adj[node]:
            if not visited[neighbor] and dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist


def dijkstra(V, edges, src):
    adj = defaultdict(list)
    for u,v,w in edges:
        adj[u].append((v,w))
    
    pq = []
    visited = [0]*V
    dist = [float('inf')]*V
    dist[src] = 0
    heapq.heappush(pq, (0, src))
    
    while pq:
        d, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = 1
        
        for neighbor, wt in adj[node]:
            if not visited[neighbor] and dist[neighbor] > d + wt:
                dist[neighbor] = d + wt
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist
