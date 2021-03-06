import copy

from graphImplementations.basicgraphs import *
from util.graphIO import *
from graphImplementations.fastgraphs import *


# Creates a graph with n vertices, with a path of length n − 1
def create_path(n):
    g = graph(n)
    for x in range(0, n - 1):
        g.addedge(g.V()[x], g.V()[x + 1])
    return g


# print("\nPath:")
# print(create_path(6))


# Creates a graph with n vertices, with a cycle of length n
def create_cycle(n):
    g = create_path(n)
    g.addedge(g.V()[0], g.V()[n - 1])
    return g


# print("\nCycle:")
# print(create_cycle(6))


# Creates a complete graph with n vertices
def create_complete(n):
    g = FastGraph(n)
    for i in g.V():
        for j in g.V():
            if i is not j:
                g.addedge(i, j)
    return g


# print("\nComplete:")
# print(create_complete(6))


#  Return a new graph that is the disjoint union of g and h
def disjointunion(g, h):
    result = FastGraph(len(g.V()) + len(h.V()))
    for edge in g.E():
        result.addedge(result.V()[edge.tail().getLabel()], result.V()[edge.head().getLabel()])
    offset = len(g.V())
    for edge in h.E():
        result.addedge(result.V()[edge.tail().getLabel() + offset], result.V()[edge.head().getLabel() + offset])
    return result


# print("\nDisjointUnion")
# g = create_complete(4)
# h = create_complete(5)
# print(disjointunion(g, h))


# Loads a graph from a text file, computes the complement, and then writes this to a new text file
# src: name of the source file
# dst: name of the destination file
def complement(src, dst):
    G = loadgraph(src)
    result = graph()
    for i in range(len(G.V())):
        result.addvertex()
    for vertex in G.V():
        for neighbour in G.V():
            if not vertex.adj(neighbour):
                result.addedge(result.__getitem__(vertex._label), result.__getitem__(neighbour._label))
    savegraph(result, dst)


# Computes the complement of a graph
def complement(g):
    result = FastGraph()
    for i in range(len(g.V())):
        result.addvertex()
    # for node in g.V():
    #     result.addObjVertex(node)
    for node in g.V():
        for neighbour in g.V():
            if not node.adj(neighbour):
                result.addedge(result.__getitem__(node.get_label()), result.__getitem__(neighbour.get_label()))
    return result


# print(complement(create_complete(6)))


def BFScheck(G, start):
    traversed = list()
    frontier = list()
    frontier.append(start)
    traversed.append(start)
    start.label = 0
    while len(frontier) > 0:
        current = frontier.pop(0)
        neighbours = current.nbs()
        for n in neighbours:
            if not n in traversed:
                frontier.append(n)
                traversed.append(n)
                n.label = len(traversed) - 1
    writeDOT(G, 'BFS.dot')
    return len(traversed) == len(G.V())


def DFScheck(G, start):
    traversed = list()
    frontier = list()
    frontier.append(start)
    traversed.append(start)
    start.label = 0
    while len(frontier) > 0:
        current = frontier.pop(len(frontier) - 1)
        neighbours = current.nbs()
        for n in neighbours:
            if not n in traversed:
                frontier.append(n)
                traversed.append(n)
                n.label = len(traversed) - 1
    writeDOT(G, 'DFS.dot')
    return len(traversed) == len(G.V())