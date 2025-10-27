# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,v):
        self.queue.append(v)
    def isempty(self):
        return(self.queue == [])
    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)    
    def __str__(self):
        return(str(self.queue))

# Function to return list of neighbours or adjacent vertex of vertex i
def neighbours(AMat,i):
    nbrs = []
    (rows,cols) = AMat.shape
    for j in range(cols):
        if AMat[i,j] == 1:
            nbrs.append(j)
    return(nbrs)

# BFS Implementation For Adjacency matrix
def BFS(AMat,start_vertex):
    # Initialization
    (rows,cols) = AMat.shape
    visited = {}
    for each_vertex in range(rows):
        visited[each_vertex] = False    
    
    # Create Queue object q
    q = Queue()
    
    # Mark the start_vertex visited and insert it into the queue 
    visited[start_vertex] = True
    q.enqueue(start_vertex)
    
    # Repeat the following until the queue is empty 
    while(not q.isempty()):
        # Remove the one vertex from queue
        curr_vertex = q.dequeue()
        # Visit the each adjacent of removed vertex(if not visited) and insert into the queue
        for adj_vertex in neighbours(AMat,curr_vertex):
            if (not visited[adj_vertex]):
                visited[adj_vertex] = True
                q.enqueue(adj_vertex)
                
    return(visited)


V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] 
size = len(V)
import numpy as np
AMat = np.zeros(shape=(size,size))
for (i,j) in E:
    AMat[i,j] = 1
print(BFS(AMat,0))