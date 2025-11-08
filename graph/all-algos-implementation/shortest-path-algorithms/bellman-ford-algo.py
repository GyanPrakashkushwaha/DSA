from typing import List, Tuple

def bellman_ford(V: int, edges: List[Tuple[int, int, int]], src: int) -> List[float]:
    
    # Step 1: Initialize distances
    dist = [float('inf')] * V
    dist[src] = 0

    # Step 2: Relax all edges V-1 times
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains a negative weight cycle")
            return []

    return dist


# Example usage:
if __name__ == "__main__":
    edges = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    V = 5
    src = 0
    print(bellman_ford(V, edges, src))
