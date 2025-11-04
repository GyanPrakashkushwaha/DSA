from multiprocessing import heap
import sys
import heapq
from collections import defaultdict

def dijkstra(V, edges, src):
    # Create adjacency list
    adj = constructAdj(edges, V)
    
    pq = [] # Create a priority queue to store vertices that are being preprocessed.
    dist = [sys.maxsize] * V # Create a list for distances and initialize all distances as infinite    
    visited = [0]*V
    
    heapq.heappush(pq, [0, src]) # Insert source itself in priority queue and initialize its distance as 0.
    dist[src] = 0

    while pq: # Looping till priority queue becomes empty (or all distances are not finalized) 
        node = heapq.heappop(pq)[1] # The first vertex in pair is the minimum distance vertex, extract it from priority queue.

        for neighbor, weight in adj[node]:
            if not visited[neighbor]:
                if dist[neighbor] > dist[node] + weight: # If there is shorter path to v through u.
                    visited[neighbor] = 1
                    dist[neighbor] = dist[node] + weight
                    heapq.heappush(pq, [dist[neighbor], neighbor])

    # Return the shortest distance array
    return dist

def dijkstra(V, edges, src):
    # Create adjacency list
    adj = constructAdj(edges, V)
    
    pq = []  # Min-heap priority queue
    dist = [sys.maxsize] * V
    visited = [0] * V
    
    heapq.heappush(pq, (0, src))
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
