Of course! Here’s a breakdown of why each problem is considered a graph problem and why it fits its specific pattern.

***

### 1. Edge List Problems ↔️

These problems define the graph's connections as a simple list of pairs.

1.  **[1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) (Easy)**
    * **Why it's a graph problem:** It deals with vertices and connections, asking for reachability (a path) between a source and destination, a fundamental graph traversal task.
    * **Why it fits the pattern:** The input `edges` is a literal list of `[u, v]` pairs, the classic edge list format.

2.  **[1791. Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/) (Easy)**
    * **Why it's a graph problem:** A "star graph" is a specific graph topology with a central node connected to all others. The problem is about identifying this central node.
    * **Why it fits the pattern:** The input is given as a list of edges, from which you must deduce the graph's structure.

3.  **[684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) (Medium)**
    * **Why it's a graph problem:** The core task is to find an edge that creates a cycle in an otherwise tree-like structure, a classic graph theory concept.
    * **Why it fits the pattern:** The input is an edge list that represents the connections being added one by one.

4.  **[785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) (Medium)**
    * **Why it's a graph problem:** Bipartition is a property of a graph where nodes can be divided into two disjoint sets such that every edge connects a node in one set to one in the other.
    * **Why it fits the pattern:** Although the input `graph` is an adjacency list, the problem can be conceptualized by its edges. Each edge `(u, v)` imposes a constraint that `u` and `v` must be in different sets. Many similar problems provide an edge list instead.

5.  **[743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Medium)**
    * **Why it's a graph problem:** It's a shortest path problem on a weighted, directed graph. The nodes are network routers, and the edges are the connections with associated travel times (weights). The goal is to find the time it takes for a signal to reach all nodes (Dijkstra's or Bellman-Ford algorithm).
    * **Why it fits the pattern:** The input `times` is a list of `[u, v, w]`, which is a weighted edge list.

6.  **[323. Number of Connected Components...](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (Medium - Premium)**
    * **Why it's a graph problem:** It asks for the number of disconnected subgraphs (connected components), a fundamental property of any graph.
    * **Why it fits the pattern:** The graph is defined by the input `edges`, a standard edge list.

7.  **[261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) (Medium - Premium)**
    * **Why it's a graph problem:** It requires checking the definition of a tree: a graph that is fully connected and has no cycles.
    * **Why it fits the pattern:** The input is an edge list that you use to build and analyze the graph structure.

8.  **[997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) (Easy)**
    * **Why it's a graph problem:** This can be modeled as a directed graph where people are nodes and a trust relationship `[a, b]` is a directed edge from `a` to `b`. The judge is a node with an in-degree of `N-1` and an out-degree of `0`.
    * **Why it fits the pattern:** The `trust` array is an edge list for a directed graph.

9.  **[1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) (Medium)**
    * **Why it's a graph problem:** The task is to find a minimum spanning tree (MST). The points are nodes, and the cost to connect any two points is the weight of the edge between them.
    * **Why it fits the pattern:** While you must first calculate all possible edges and their weights from the `points` coordinates, the core algorithms (Kruskal's or Prim's) operate on this generated list of edges.

10. **[310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) (Medium)**
    * **Why it's a graph problem:** The goal is to find the central nodes in a tree (a type of graph) that minimize the longest path to any leaf.
    * **Why it fits the pattern:** The input is an `edges` list, which you use to build the tree structure.

***

### 2. Adjacency List Problems 🗺️

These problems provide a direct mapping from each node to its neighbors.

1.  **[133. Clone Graph](https://leetcode.com/problems/clone-graph/) (Medium)**
    * **Why it's a graph problem:** The input is an interconnected structure of `Node` objects, which is by definition a graph.
    * **Why it fits the pattern:** The `Node` class contains a `neighbors` list. This `node -> neighbors` relationship is a direct, object-oriented form of an adjacency list.

2.  **[797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) (Medium)**
    * **Why it's a graph problem:** Finding all possible paths between two nodes is a classic graph traversal problem.
    * **Why it fits the pattern:** The input `graph` is a literal adjacency list, where `graph[i]` is a list of nodes reachable from node `i`.

3.  **[207. Course Schedule](https://leetcode.com/problems/course-schedule/) (Medium)**
    * **Why it's a graph problem:** This is about finding cycles in a directed graph. Courses are nodes, and prerequisites are directed edges. A cycle means an impossible schedule.
    * **Why it fits the pattern:** While the input is an edge list (`prerequisites`), the standard solution involves first building an adjacency list to efficiently perform a topological sort (or cycle detection). The logic operates on the adjacency list.

4.  **[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (Medium)**
    * **Why it's a graph problem:** A follow-up to the above, this requires finding a valid topological sort ordering of the course graph.
    * **Why it fits the pattern:** Like its predecessor, the problem is best solved by converting the input edge list into an adjacency list to run the topological sort algorithm.

5.  **[841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) (Medium)**
    * **Why it's a graph problem:** Rooms are nodes, and having a key to another room is a directed edge. The problem asks if all nodes are reachable from node 0.
    * **Why it fits the pattern:** The input `rooms` is a direct adjacency list, where `rooms[i]` is the list of keys (and thus accessible rooms) found in room `i`.

6.  **[332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) (Hard)**
    * **Why it's a graph problem:** This is a quest to find a specific path (an Eulerian path) that uses every edge exactly once. Airports are nodes, and flights are directed edges.
    * **Why it fits the pattern:** The solution requires building an adjacency list from the `tickets` (edge list) to efficiently find the next flight from a given airport in lexicographical order.

7.  **[802. Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) (Medium)**
    * **Why it's a graph problem:** It asks to identify all nodes in a directed graph from which every possible path leads to a "terminal" node (one with no outgoing edges), i.e., nodes not part of a cycle.
    * **Why it fits the pattern:** The input `graph` is a direct adjacency list representation.

8.  **[886. Possible Bipartition](https://leetcode.com/problems/possible-bipartition/) (Medium)**
    * **Why it's a graph problem:** This is identical in structure to "Is Graph Bipartite?". People are nodes, and a dislike relationship is an edge. You need to see if they can be split into two groups.
    * **Why it fits the pattern:** You first convert the `dislikes` edge list into an adjacency list to efficiently traverse the graph and assign nodes to groups.

9.  **[417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) (Medium)**
    * **Why it's a graph problem:** Water flow can be modeled as a directed graph where an edge exists from a higher cell to an adjacent lower or equal cell. The problem asks which nodes can reach both the "Pacific" and "Atlantic" sets of nodes.
    * **Why it fits the pattern:** While the input is a grid, the solution typically involves two separate graph traversals (BFS/DFS), one starting from each ocean. You can think of the grid itself as an adjacency list where neighbors are calculated implicitly.

10. **[1466. Reorder Routes to Make All Paths...](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)**
    * **Why it's a graph problem:** Roads are edges and cities are nodes. The task is to orient the edges such that node 0 is reachable from all other nodes. This involves traversing the graph to find misaligned edges.
    * **Why it fits the pattern:** The most effective way to solve this is to build an adjacency list that stores both the original direction and its reverse, allowing you to traverse the underlying undirected structure while checking edge orientations.

***

### 3. Grid (Implicit Graph) Problems 🌐

The graph is implicitly defined by a 2D matrix, where adjacency is based on position.

1.  **[200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium)**
    * **Why it's a graph problem:** Land cells ('1') are nodes, and adjacency creates edges. An "island" is a connected component in this graph.
    * **Why it fits the pattern:** The input is a 2D `grid`. The graph is implicit in the grid's structure.

2.  **[695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) (Medium)**
    * **Why it's a graph problem:** A follow-up to "Number of Islands," this asks for the size of the largest connected component.
    * **Why it fits the pattern:** It's an implicit graph defined by a 2D `grid`.

3.  **[994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (Medium)**
    * **Why it's a graph problem:** This is a shortest path problem on an unweighted graph, solved with a multi-source BFS. Oranges are nodes, and adjacency allows rotting to spread.
    * **Why it fits the pattern:** The `grid` input defines the nodes and their positions, making it an implicit graph problem.

4.  **[542. 01 Matrix](https://leetcode.com/problems/01-matrix/) (Medium)**
    * **Why it's a graph problem:** This is another shortest path problem where you find the distance from every node ('1') to the nearest source node ('0').
    * **Why it fits the pattern:** The problem is set on a 2D `grid`, where distance is measured between adjacent cells.

5.  **[130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (Medium)**
    * **Why it's a graph problem:** The 'O's are nodes. An 'O' is captured if it's not part of a connected component that touches the border of the grid.
    * **Why it fits the pattern:** The problem is defined on a 2D `board`, an implicit grid graph.

6.  **[79. Word Search](https://leetcode.com/problems/word-search/) (Medium)**
    * **Why it's a graph problem:** This is a path-finding problem (using DFS/backtracking). The cells are nodes, and you can form a path by moving between adjacent cells.
    * **Why it fits the pattern:** The search space is a 2D `board` of characters.

7.  **[1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) (Medium)**
    * **Why it's a graph problem:** A classic shortest path (BFS) problem on an unweighted graph from a start node (top-left) to an end node (bottom-right).
    * **Why it fits the pattern:** The pathfinding occurs on a 2D `grid`.

8.  **[733. Flood Fill](https://leetcode.com/problems/flood-fill/) (Easy)**
    * **Why it's a graph problem:** This is a graph traversal (BFS/DFS) problem where you find a connected component of cells with the same color starting from a given cell and change their color.
    * **Why it fits the pattern:** The `image` is a 2D grid that defines the graph.

9.  **[1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) (Medium)**
    * **Why it's a graph problem:** It asks to count the number of connected components ('0's) that are not connected to the boundary of the graph.
    * **Why it fits the pattern:** The graph of land and water is represented by a 2D `grid`.

10. **[286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/) (Medium - Premium)**
    * **Why it's a graph problem:** This is a multi-source BFS problem to find the shortest distance from every "room" node to the nearest "gate" node.
    * **Why it fits the pattern:** The `rooms` are laid out in a 2D grid, defining the implicit graph structure.

***

### 4. Adjacency Matrix Problems 🔢

These problems either use an `N x N` matrix input or are best solved by creating one.

1.  **[547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) (Medium)**
    * **Why it's a graph problem:** Cities are nodes, connections are edges, and provinces are connected components.
    * **Why it fits the pattern:** The input `isConnected` is a textbook `N x N` adjacency matrix where `isConnected[i][j] == 1` denotes an edge.

2.  **[1334. Find the City With the Smallest Number of Neighbors...](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) (Medium)**
    * **Why it's a graph problem:** It's an all-pairs shortest path problem. Cities are nodes, and roads are weighted edges.
    * **Why it fits the pattern:** The Floyd-Warshall algorithm, a classic solution for this, operates on an adjacency matrix. So, the standard approach is to convert the input edge list into an adjacency matrix first.

3.  **[277. Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) (Medium - Premium)**
    * **Why it's a graph problem:** People are nodes, and `knows(a, b)` defines a directed edge. A celebrity is a node with `N-1` in-degree and `0` out-degree.
    * **Why it fits the pattern:** The `knows(i, j)` API functions exactly like accessing `matrix[i][j]` in an adjacency matrix, even though you don't build the matrix explicitly.

4.  **[847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) (Hard)**
    * **Why it's a graph problem:** A complex shortest path problem where the "state" in your traversal needs to include not just the current node, but also a bitmask of all visited nodes.
    * **Why it fits the pattern:** For problems with a small number of nodes (N <= 16), an adjacency matrix is a very common and efficient way to store connections, especially when used with bitmask DP solutions. The input is an adjacency list, but the solution pattern often resembles matrix-based approaches.

5.  **[924. Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/) (Hard)**
    * **Why it's a graph problem:** The network is a graph, and malware spreads through its connected components. The goal is to find a node whose removal minimizes the size of the largest infected component.
    * **Why it fits the pattern:** The input `graph` is a direct `N x N` adjacency matrix.

6.  **[851. Loud and Rich](https://leetcode.com/problems/loud-and-rich/) (Medium)**
    * **Why it's a graph problem:** People are nodes, and a "richer" relationship is a directed edge. For each person, you need to find the quietest person in the subgraph of people richer than or equal to them.
    * **Why it fits the pattern:** While the input is an edge list, the problem can be solved by building a full graph representation (adjacency list or matrix) and performing a DFS/BFS from each node.

7.  **[1129. Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/) (Medium)**
    * **Why it's a graph problem:** A variation of the shortest path problem where edges have colors, and the path must alternate between them.
    * **Why it fits the pattern:** You are given two separate edge lists, one for each color. This can be conceptualized as two separate adjacency matrices/lists that the traversal algorithm must switch between.

8.  **[787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (Medium)**
    * **Why it's a graph problem:** A shortest path problem (airports are nodes, flights are weighted edges) with an additional constraint on the number of edges in the path. This is a variation of Bellman-Ford or Dijkstra's algorithm.
    * **Why it fits the pattern:** A common approach for Bellman-Ford involves iteratively updating distances, which can be organized in a way that relates to the adjacency matrix structure, although it's often implemented with an edge list for efficiency.

9.  **[1462. Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/) (Medium)**
    * **Why it's a graph problem:** You need to determine reachability between pairs of nodes in a directed acyclic graph (courses and their prerequisites).
    * **Why it fits the pattern:** The most direct way to answer many reachability queries is to pre-compute the transitive closure of the graph. The Floyd-Warshall algorithm does this naturally and operates on an adjacency matrix.

10. **[1557. Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) (Medium)**
    * **Why it's a graph problem:** The task is to find the smallest set of source nodes in a directed graph from which all other nodes can be reached. This boils down to finding all nodes with an in-degree of 0.
    * **Why it fits the pattern:** While solvable with an in-degree array built from the input edge list, this concept is fundamentally tied to the properties of nodes within the graph's overall structure, which can be represented by either an adjacency list or matrix.