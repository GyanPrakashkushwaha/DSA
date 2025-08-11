from collections import deque

class Solution:
    def __init__(self):
        self.visited = None

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        return self.countProvinces(isConnected)
    
    def bfs(self, adjMatrix, start): # BFS Algorithm without a single change
        queue = deque([start])
        self.visited[start] = 1
        while queue:
            node = queue.popleft()
            for neighbor in range(len(adjMatrix[node])):
                if adjMatrix[node][neighbor] == 1 and node != neighbor and not self.visited[neighbor]:
                    self.visited[neighbor] = 1
                    queue.append(neighbor)
            
    def countProvinces(self, adjMatrix): # Very straight forward! Simply calling the BFS for all nodes for the disconnected graph.
        self.visited = [0]*len(adjMatrix)
        provinces = 0
        for city in range(len(adjMatrix)):
            if not self.visited[city]:
                provinces += 1
                self.bfs(adjMatrix, city)
        
        return provinces
    
    
from collections import deque

class Solution:
    def __init__(self):
        self.visited = None

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = [0]*len(isConnected)
        provinces = 0
        for city in range(len(isConnected)):
            if not self.visited[city]:
                provinces += 1
                self.bfs(isConnected, city)
        
        return provinces

    
    def bfs(self, adjMatrix, start): 
        queue = deque([start])
        self.visited[start] = 1
        while queue:
            node = queue.popleft()
            for neighbor in range(len(adjMatrix[node])):
                if adjMatrix[node][neighbor] == 1 \
                 and node != neighbor \
                 and not self.visited[neighbor]:
                    self.visited[neighbor] = 1
                    queue.append(neighbor)
            
