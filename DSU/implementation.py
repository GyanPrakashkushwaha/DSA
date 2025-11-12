class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb: return

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

dsu = DSU(5)
dsu.union(0, 1)
dsu.union(2, 3)
dsu.union(1, 3)
dsu.union(3, 4)
dsu.find(3)
dsu.find(4)