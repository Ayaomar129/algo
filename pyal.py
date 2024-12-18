class edge :
    def __init__(self, vertex1,vertex2,weight):
        self.vertex1=vertex1
        self.vertex2=vertex2
        self.weight=weight
class graph :
    def __init__(self,edges=None):
        self .vertices ={}
        self.edges=[]
        if edges is not None :
            for edge in edges:
                self.addedge(edge)

    def addedge(self,edge,isdirected=False):
        self.edges.append(edge)
        if edge.vertex1 not in self.vertices:
            self.vertices[edge.vertex1]=[]
        if edge.vertex2 not in self.vertices:
            self.vertices[edge.vertex2]=[]
        self.vertices [edge.vertex1].append((edge.vertex2,edge.weight))
        if not isdirected:
            self.vertices [edge.vertex2].append((edge.vertex1,edge.weight))
    def removeedge(self,edge,isdirected=False):
        self.edges.remove(edge)
        self.vertices [edge.vertex1].remove((edge.vertex2,edge.weight))
        if not isdirected:
            self.vertices [edge.vertex2].append((edge.vertex1,edge.weight))
        
    def printg(self):
        print ("num of edge",len(self.vertices))
        keys=self.vertices.keys()
        for key in keys :
            print (key,":",end=" ")
    def printe(self):
        for edge in self.edges:
            print(edge.getEdgeDetails())
    def sorte(self):
        edgeList=self.edges[:]
        from operator import attrgetter
        edgeList.sort(key=attrgetter('weight'),reverse=False)
        return edgeList
    def kruskal(self):
        mst=graph()
        edgeList=self.sorte()
        for edge in edgeList:
            print ("adding edge ",edge.getEdgeDetails())
            mst.addedge(edge)
            set1=set(mst.vertices[edge.vertex1])
            set2=set(mst.vertices[edge.vertex2])
            set3=set1.intersection(set2)
            print("==============")
            print(set1,set2)
            print(set3)
        return mst
def main ():
    edge0=edge(0,1,4)
    edge1=edge(0,2,4)
    for edge in edges:
        print (edge.getEdgeDetails())
    g=graph(edges)
    graph.printg()
    graph.printe()
    mst=graph.kruskal()
    mst.printg()
    mst.printe()
    main()