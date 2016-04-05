from graphImplementations.fastgraphs import FastVertex, FastGraph
from util.graphutil import create_complete
from util.graph_generator import *

def istree(graph):
    node = graph.V()[3]
    if len(dfs(graph, node)) == len(graph.V()):
        return True
    else:
        return False

def dfs(graph, start, visited = [], exploredEdges = []):
    visited.append(start)
    for next in start.nbs():
        edge = graph.findedge(start, next)
        otherEdge = graph.findedge(next, start)
        if edge not in exploredEdges and otherEdge not in exploredEdges:
            exploredEdges.append(edge)
            exploredEdges.append(otherEdge)
            dfs(graph, next, visited, exploredEdges)
    return visited

graph = loadgraph("C:/Users/GIJS-PC/PycharmProjects/Similarity-and-Symmetry/lfn/testGraphs/bigtrees2.grl", FastGraph)
# graph.addedge(graph.V()[4], graph.V()[6])
# graph.addedge(graph.V()[6], graph.V()[7])
# graph.addedge(graph.V()[7], graph.V()[4])
writeDOT(graph, "deze")

print(istree(graph))