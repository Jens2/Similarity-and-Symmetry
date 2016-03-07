from util.graphIO import loadgraph, writeDOT  # graphIO imports basicgraphs.py, so we do not need to import it here.

# Use these options to change the tests:

TestBellmanFordDirected = False
TestBellmanFordUndirected = False
TestDijkstraDirected = True
TestDijkstraUndirected = False
TestKruskal = False

WriteDOTFiles = True

# Use these options to select the graphs to test your algorithms on:
# TestInstances = ["weightedexample.gr"]
# TestInstances=["randomplanar.gr"]
# TestInstances=["negativeweightexample.gr"]
# TestInstances=["negativeweightcycleexample.gr"]
# TestInstances=["WDE100.gr","WDE200.gr","WDE400.gr","WDE800.gr","WDE2000.gr"]; WriteDOTFiles=False
TestInstances=["bbf2000.gr"]
# TestInstances = ["graph1.gr", "graph2.gr", "graph3.gr", "graph4.gr", "graph5.gr", "graph6.gr", "graph7.gr"]; WriteDotFiles = False

# If you have implemented a module fastgraphs.py (compatible with basicgraphs.py),
# you can set this option to True:
UseFastGraphs = True


def relax(G, weight, v, w):
    # w = e.head()
    # v = e.tail()
    if v.dist is None:
        return False
    if w.dist is None or w.dist > v.dist + weight:
        w.dist = v.dist + weight
        w.inedge = v
        return True

def getSmallestVertex(V):
    old = next(iter(V))
    for vertex in V:
        if vertex.dist is not None:
            if old.dist is None or vertex.dist < old.dist:
                old = vertex
    return old


def checkForNegativeWeightCycle(e):
    w = e.head()
    v = e.tail()
    if v.dist is None:
        return False
    if w.dist is None or w.dist > (v.dist + e.weight):
        return True


def BellmanFordUndirected(G, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <indedge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as an undirected graph.
    """
    # Initialize the vertex attributes:
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0

    for i in range(1, len(G.V())):
        for edge in G.E():
            relax(G, edge.weight, edge.tail(), edge.head())
            relax(G, edge.weight, edge.head(), edge.tail())


# Insert your code here.



def BellmanFordDirected(G, start):
    # """
    # Arguments: <G> is a graph object, where edges have integer <weight>
    # 	attributes,	and <start> is a vertex of <G>.
    # Action: Uses the Bellman-Ford algorithm to compute all vertex distances
    # 	from <start> in <G>, and assigns these values to the vertex attribute <dist>.
    # 	Optional: assigns the vertex attribute <indedge> to be the incoming
    # 	shortest path edge, for every reachable vertex except <start>.
    # 	<G> is viewed as a directed graph.
    # """
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0

    for i in range(1, len(G.V())):
        for edge in G.E():
            relax(G, edge.weight, edge.tail(), edge.head())
    for edge in (G.E()):
        if checkForNegativeWeightCycle(edge):
            print("\n*******************************\n"
                  "Negative weight cycle detected!\n"
                  "*******************************\n")
            break


def DijkstraUndirected(G, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <indedge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as an undirected graph.
    """
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0

    S = set()
    V = set(G.V())
    while S < V:
        v = getSmallestVertex(V - S)
        S.add(v)
        for edge in v.inclist():
            relax(G, edge.weight, edge.tail(), edge.head())
            relax(G, edge.weight, edge.head(), edge.tail())


def DijkstraDirected(G, start):
    # """
    # Arguments: <G> is a graph object, where edges have integer <weight>
    # attributes,	and <start> is a vertex of <G>.
    # Action: Uses Dijkstra's algorithm to compute all vertex distances
    # from <start> in <G>, and assigns these values to the vertex attribute <dist>.
    # Optional: assigns the vertex attribute <indedge> to be the incoming
    # shortest path edge, for every reachable vertex except <start>.
    # <G> is viewed as a directed graph.
    # """
    #
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0

    S = set()
    V = set(G.V())
    while S < V:
        v = getSmallestVertex(V - S)
        S.add(v)
        for edge in v.inclist():
            relax(G, edge.weight, edge.tail(), edge.head())


def Kruskal(G):
    """
    Arguments: <G> is a graph object, where edges have integer <weight> attributes.
    Action: Uses Kruskal's algorithm to compute all a minimum weight spanning tree
        of <G> (or a minimum weight maximal spanning forest if <G> is not connected).
        Returns a list <ST> of all edges that are in the minimum weight spanning
        tree (forest).
    """
    ST = []  # will be the spanning tree. Append edge objects to this list.

    # Insert your code here.

    return ST


##############################################################################
#
# Below is test code that does not need to be changed.
#
##############################################################################

def printmaxdist(G):
    unreachable = False
    numreachable = 0
    unreachablev = []
    remote = G[0]
    for v in G:
        if v.dist == None:
            unreachable = True
            unreachablev.append(v)
        # print("Vertex",v,"is unreachable")
        else:
            numreachable += 1
            if remote.dist == None or v.dist > remote.dist:
                remote = v
    print("Number of reachable vertices:", numreachable, "out of", len(G.V()))
    if (len(G.V()) - numreachable > 0):
        print("Vertices that are unreachabe:", *unreachablev)
    print("Largest distance:", remote.dist, "For vertex", remote)


def preparedrawing(G):
    for e in G.E():
        e.colornum = 0
    for v in G.V():
        if hasattr(v, "inedge") and v.inedge != None:
            v.inedge.colornum = 1
    for v in G:
        if v.dist != None:
            v.label = v.dist
        else:
            v.label = "inf"


if __name__ == "__main__":
    from time import time

    if UseFastGraphs:
        import fastgraphs
    for FileName in TestInstances:
        if UseFastGraphs:
            print("\n\nLoading graph", FileName, "(Fast graph)")
            # G=loadgraph("graphs/"+FileName,graph)
            G = loadgraph(FileName, fastgraphs.graph)
        else:
            print("\n\nLoading graph", FileName)
            # G=loadgraph("graphs/"+FileName)
            G = loadgraph(FileName)

        for i in range(len(G.V())):
            G[i].colornum = i

        # Tuple arguments below:
        # First: printable string
        # Second: Boolean variable: should test be done?
        # Third: Function
        # Fourth: Filename
        # Fifth: Whether output should be directed
        for testalg in [("Bellman-Ford, undirected", TestBellmanFordUndirected, BellmanFordUndirected,
                         "BellmanFordUndirected", False),
                        ("Bellman-Ford, directed", TestBellmanFordDirected, BellmanFordDirected, "BellmanFordDirected",
                         True),
                        ("Dijkstra, undirected", TestDijkstraUndirected, DijkstraUndirected, "DijkstraUndirected",
                         False),
                        ("Dijkstra, directed", TestDijkstraDirected, DijkstraDirected, "DijkstraDirected", True),
                        ("Kruskal", TestKruskal, Kruskal, "Kruskal", False)]:
            if testalg[1]:
                print("\n\nTesting", testalg[0])
                startt = time()
                if testalg[0] == "Kruskal":
                    ST = testalg[2](G)
                    totalweight = 0
                    for e in ST:
                        totalweight += e.weight
                else:
                    testalg[2](G, G[0])
                endt = time()
                print("Elapsed time in seconds:", endt - startt)

                if testalg[0] != "Kruskal":
                    printmaxdist(G)
                    preparedrawing(G)
                else:
                    if len(ST) < len(G.V()) - 1:
                        print("Total weight of maximal spanning forest:", totalweight)
                    else:
                        print("Total weight of spanning tree:", totalweight)
                    for e in G.E():
                        e.colornum = 0
                    for e in ST:
                        e.colornum = 1
                    for v in G.V():
                        print()
                        # v.label = v._label

                if WriteDOTFiles:
                    # writeDOT(G,'graphs/'+testalg[3]+'.dot',directed=testalg[4])
                    writeDOT(G, testalg[3] + '.dot', directed=testalg[4])
