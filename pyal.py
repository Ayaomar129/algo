class edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def getEdgeDetails(self):
        return f"({self.vertex1}, {self.vertex2}, weight={self.weight})"


class graph:
    def __init__(self, edges=None):
        self.vertices = {}
        self.edges = []
        if edges is not None:
            for edge in edges:
                self.addedge(edge)

    def addedge(self, edge, isdirected=False):
        self.edges.append(edge)
        if edge.vertex1 not in self.vertices:
            self.vertices[edge.vertex1] = []
        if edge.vertex2 not in self.vertices:
            self.vertices[edge.vertex2] = []
        self.vertices[edge.vertex1].append((edge.vertex2, edge.weight))
        if not isdirected:
            self.vertices[edge.vertex2].append((edge.vertex1, edge.weight))

    def removeedge(self, edge, isdirected=False):
        self.edges.remove(edge)
        self.vertices[edge.vertex1].remove((edge.vertex2, edge.weight))
        if not isdirected:
            self.vertices[edge.vertex2].remove((edge.vertex1, edge.weight))

    def printg(self):
        print("Number of edges:", len(self.edges))
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex} -> {neighbors}")

    def printe(self):
        for edge in self.edges:
            print(edge.getEdgeDetails())

    def sorte(self):
        # Sort the edges by weight
        return sorted(self.edges, key=lambda e: e.weight)

    def kruskal(self):
        # Helper functions for Kruskal's Algorithm
        parent = {}
        rank = {}

        def find(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])  # Path compression
            return parent[vertex]

        def union(vertex1, vertex2):
            root1 = find(vertex1)
            root2 = find(vertex2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        # Initialize the disjoint set
        for vertex in self.vertices:
            parent[vertex] = vertex
            rank[vertex] = 0

        mst = graph()
        edgeList = self.sorte()

        for edge in edgeList:
            root1 = find(edge.vertex1)
            root2 = find(edge.vertex2)

            # If adding this edge doesn't form a cycle
            if root1 != root2:
                mst.addedge(edge)
                union(edge.vertex1, edge.vertex2)

        return mst


def main():
    # Create edges
    edge0 = edge(0, 1, 4)
    edge1 = edge(0, 2, 3)
    edge2 = edge(1, 2, 1)
    edge3 = edge(1, 3, 2)
    edge4 = edge(2, 3, 5)

    # List of edges
    edges = [edge0, edge1, edge2, edge3, edge4]

    # Create graph
    g = graph(edges)

    print("Original Graph:")
    g.printg()
    g.printe()

    print("\nMinimum Spanning Tree (Kruskal's Algorithm):")
    mst = g.kruskal()
    mst.printg()
    mst.printe()


main()
