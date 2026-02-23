class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])   
        return self.parent[x]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u != parent_u:
            # Union by rank
            if self.rank[parent_u] < self.rank[parent_v]:
                self.parent[parent_u] = parent_v
            elif self.rank[parent_v] < self.rank[parent_u]:
                self.parent[parent_v] = parent_u
            else:
                self.parent[parent_u] = parent_v
                self.rank[parent_v] += 1

def kruskal(V, edges):
    # V = number of vertices (0 to V-1)
    # edges = list of (weight, u, v)
    edges.sort() 
    ds = DisjointSet(V)
    A = []         
    mst_weight=0
    # Step 5–9
    for w, u, v in edges:
        # if no cycle
        if ds.find(u) != ds.find(v):  
            # add edge to MST
            A.append((u, v, w))       
            ds.union(u, v)
            mst_weight+=w

    return A,mst_weight

V = 4
edges = [
    (1, 0, 1),
    (4, 0, 2),
    (3, 1, 2),
    (2, 1, 3),
    (5, 2, 3)
]

mst = kruskal(V, edges)
for u, v, w in mst[0]:
    print(u, "-", v, "weight:", w)
print()
print(f"Total weight is: {mst[1]}")
