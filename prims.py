class graph:
    def __init__(self):
        self.edges = []
        self.vertices = set()

    def add_edge(self,u,v,w):
        self.edges.append((u,v,w))
        self.vertices.add(u)
        self.vertices.add(v)

    def prim(self,start):
        visited = set([start])
        mst = []
        total_cost = 0

        while len(visited) < len(self.vertices):
            min_edges = None
            min_weight = float('inf')

            for u,v,w in self.edges :
                if u in visited and v not in visited and w < min_weight:
                    min_weight = w
                    min_edge = (u,v,w)

                    if min_edge is None:
                        break

                    u,v,w = min_edge 
                    visited.add(v)
                    mst.append((u,v,w))
                    total_cost+=w

        print("\n Edges in Minimum cost spanning Tree:")
        for u,v,w in mst:
            print(f"{u}-{v}={w}")

        print("Total cost of MST: ",total_cost)

g = graph()
e = int(input("Enter number of edges:"))
print("Enter edges in format : ab3")
for _ in range(e):
    edge,weight = input().split()
    u = edge[0]
    v = edge[1]
    w = int(weight)
    g.add_edge(u,v,w)

start = input("Enter starting vertex :")
g.prim(start)

