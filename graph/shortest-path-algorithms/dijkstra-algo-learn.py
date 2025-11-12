from collections import defaultdict
import heapq

def dijkstraAlgo(edges, V, src):
    adjList = defaultdict(list)
    for node, neighbor, edgeWeight in edges:
        adjList[node].append((neighbor, edgeWeight))
        adjList[neighbor].append((node, edgeWeight))
    
    visited = [0]*V
    dist = [float('inf')]*V
    dist[src] = 0 # 0--distance
    pq = [(0, src)]
    
    # main Loop
    while pq:
        dis, node = heapq.heappop(pq)
        if visited[node]: continue
        visited[node] = 1
        
        # relaxation
        for adjacent, edgeWt in adjList[node]:
            # updation...
            if not visited[adjacent] and dis + edgeWt < dist[adjacent]:
                dist[adjacent] = dis + edgeWt
                heapq.heappush(pq, (dist[adjacent], adjacent))
            
    return dist
        
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (1, 2, 2),
    (1, 3, 3),
    (2, 3, 5)
]

V = 4
src = 0

print(dijkstraAlgo(edges, V, src))
    

def dijkstraSet(self, V, edges, src):
    adjList = defaultdict(list)
    for node, neighbor, edgeWeight in edges:
        adjList[node].append((neighbor, edgeWeight))
        adjList[neighbor].append((node, edgeWeight))
    
    dist = [float('inf')]*V
    dist[src] = 0 
    st = {(0, src)}
    
    while st:
        dis, node = min(st)
        st.remove((dis, node))
        for adjacent, edgeWt in adjList[node]:
            if dis + edgeWt < dist[adjacent]:
                if (dist[adjacent], adjacent) in st:
                    st.remove((dist[adjacent], adjacent))
                dist[adjacent] = dis + edgeWt
                st.add((dist[adjacent], adjacent))
            
    return dist