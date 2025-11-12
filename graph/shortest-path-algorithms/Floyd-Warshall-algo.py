# Floyd-Warshall using adjacency matrix

def floyd_warshall_matrix(graph):
    V = len(graph)
    dist = [row[:] for row in graph]  # copy of graph

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


# Example
INF = float('inf')
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

dist = floyd_warshall_matrix(graph)

print("Shortest distance matrix:")
for row in dist:
    print(row)
