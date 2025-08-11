Of course\! Here are the common implementation patterns for the four graph representations you've identified in LeetCode problems. The most frequent task is to traverse the graph, so these examples focus on setting up for a Breadth-First Search (BFS) or Depth-First Search (DFS). The key is almost always to get to an **Adjacency List** representation, as it's the most efficient for finding a node's neighbors.

-----

### 1\. Edge List ↔️

An **Edge List** is a simple list of pairs, where each pair `[u, v]` represents an edge between node `u` and node `v`. This format is easy to read but inefficient for finding neighbors.

The most common pattern is to **convert the edge list into an adjacency list** before doing anything else.

#### Implementation

```python
from collections import defaultdict

def build_adj_list_from_edges(n: int, edges: list[list[int]]) -> dict[int, list[int]]:
    """
    Builds an adjacency list from a number of nodes (n) and an edge list.
    """
    adj = defaultdict(list)
    for u, v in edges:
        # For an undirected graph, add edges in both directions
        adj[u].append(v)
        adj[v].append(u)
    return adj

# --- Example Usage ---
num_nodes = 4
edge_list = [[0, 1], [0, 2], [1, 2], [2, 3]]

# Convert to an adjacency list
adjacency_list = build_adj_list_from_edges(num_nodes, edge_list)

# The result is ready for traversal algorithms like BFS or DFS
# {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
print(dict(adjacency_list))
```

**Key Idea:** Iterate through the edges once to build a hash map (or dictionary) where each node maps to a list of its direct neighbors.

-----

### 2\. Adjacency List 🗺️

An **Adjacency List** is the most common and efficient representation for sparse graphs on LeetCode. It's typically a dictionary or an array of lists, where the key/index represents a node and the value is a list of its neighbors.

Problems often give you the graph in this format, or you convert it from an edge list as shown above. Traversing it is straightforward.

#### Implementation

```python
from collections import deque

def bfs_on_adj_list(adj: dict[int, list[int]], start_node: int):
    """
    Performs a standard BFS traversal on an adjacency list.
    """
    if not adj or start_node not in adj:
        return []

    queue = deque([start_node])
    visited = {start_node}
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        # Simply look up neighbors in the adjacency list
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

# --- Example Usage ---
# Assume this adjacency list is given or was built from an edge list
adjacency_list = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}

# Perform BFS starting from node 0
order = bfs_on_adj_list(adjacency_list, 0)

# Example output: [0, 1, 2, 3]
print(order)
```

**Key Idea:** An adjacency list gives you direct O(1) access to the list of neighbors for any node, making traversals very efficient.

-----

### 3\. Grid (Implicit Graph) 🌐

A **Grid** (or 2D matrix) is an **implicit graph**. Each cell `(r, c)` is a node. Its neighbors are the adjacent cells (typically up, down, left, and right). You don't build a separate adjacency list; instead, you calculate neighbors on the fly.

The common pattern is to use a `directions` array to explore neighbors and check for boundary conditions.

#### Implementation

```python
from collections import deque

def bfs_on_grid(grid: list[list[int]], start_r: int, start_c: int):
    """
    Performs a BFS on a grid, treating it as an implicit graph.
    Assumes `1` is traversable land and `0` is water.
    """
    if not grid or grid[start_r][start_c] == 0:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_r, start_c)])
    visited = {(start_r, start_c)}
    count = 0

    # Directions for neighbors: Right, Left, Down, Up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c = queue.popleft()
        count += 1  # Process the cell (e.g., count it)

        # Calculate and explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check for valid neighbors:
            # 1. Within grid boundaries
            # 2. Not visited yet
            # 3. Is a valid path (e.g., not water)
            if 0 <= nr < rows and 0 <= nc < cols and \
               (nr, nc) not in visited and grid[nr][nc] == 1:
                visited.add((nr, nc))
                queue.append((nr, nc))
                
    return count

# --- Example Usage ---
grid = [
  [1, 1, 0, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 0],
  [0, 0, 0, 1]
]

# Find the size of the island starting at (0, 0)
island_size = bfs_on_grid(grid, 0, 0)

# Output: 6
print(island_size)
```

**Key Idea:** The graph structure is defined by the grid's geometry. Use a `directions` array and boundary checks to find neighbors during traversal.

-----

### 4\. Adjacency Matrix 🔢

An **Adjacency Matrix** is a `N x N` matrix where `matrix[i][j] = 1` (or a weight) indicates an edge from node `i` to node `j`. This is common for dense graphs where the number of edges is close to the number of nodes squared.

To find the neighbors of a node `i`, you must **iterate through the entire `i`-th row**.

#### Implementation

```python
from collections import deque

def bfs_on_adj_matrix(matrix: list[list[int]], start_node: int):
    """
    Performs a BFS on an adjacency matrix.
    """
    num_nodes = len(matrix)
    if num_nodes == 0:
        return []
        
    queue = deque([start_node])
    visited = {start_node}
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        # To find neighbors, iterate through the node's row
        for neighbor in range(num_nodes):
            # If matrix[node][neighbor] is 1, an edge exists
            if matrix[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

# --- Example Usage ---
# Adjacency matrix for a fully connected graph of 3 nodes
adj_matrix = [
  [0, 1, 1],  # Node 0 is connected to 1 and 2
  [1, 0, 1],  # Node 1 is connected to 0 and 2
  [1, 1, 0]   # Node 2 is connected to 0 and 1
]

# Perform BFS starting from node 0
order = bfs_on_adj_matrix(adj_matrix, 0)

# Example output: [0, 1, 2]
print(order)
```

**Key Idea:** Finding neighbors for node `i` requires a linear scan of row `i`, which takes $O(N)$ time, where $N$ is the number of nodes. This is less efficient than an adjacency list for sparse graphs.