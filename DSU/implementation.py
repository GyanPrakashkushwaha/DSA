class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        pa = self.find(a)
        pa = self.find(b)
        if pa == pb: return

        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        self.parent[pb] = ra
        self.size[pa] += self.size[pb]

dsu = DSU(5)
dsu.union(0, 1)
dsu.union(2, 3)
dsu.union(1, 3)
dsu.union(3, 4)
dsu.find(3)
dsu.find(4)