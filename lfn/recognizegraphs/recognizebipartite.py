from graphImplementations.fastgraphs import FastVertex, FastGraph
from util.graphutil import create_complete
from util.graph_generator import *

ZWART = 1
ROOD = 0
NULL = -1

def isbipartite(graph):
    vertices = graph.V()
    colorList = [NULL] * len(vertices)

    colorList[vertices[0]._label] = ZWART
    for vertex in vertices:
        for neighbour in vertex.nbs():
            if colorList[neighbour._label] == NULL:
                colorList[neighbour._label] = othercolor(vertex, colorList)
            else:
                if colorList[vertex._label] == colorList[neighbour._label]:
                    return False
    return True

def othercolor(vertex, colorList):
    color = colorList[vertex._label]
    if color == NULL:
        return NULL
    if color == ZWART:
        return ROOD
    if color == ROOD:
        return ZWART