from graphImplementations.fastgraphs import *

#  Return a new graph that is the disjoint union of g and h
def disjointunion(g, h):
    result = g
    hcopy = h
    listofvertices = []
    length = len(g.V())
    for vertex in hcopy.V():
        vertex._label += length
        vertex.setGraph(result)
        node = result.addvertex(vertex.getLabel())
        listofvertices.append(node)
    for edge in hcopy.E():
        for node in listofvertices:
            # print(type(node._label))
            if edge.tail().getLabel() is node.getLabel():
                edge.setTail(node)
            elif edge.head().getLabel() is node.getLabel():
                edge.setHead(node)
        result.addedge(edge.tail(), edge.head())
    # for node in result:
    #     print(type(node.getLabel()))
    return result




def disjoint_union(g, h):
    result = FastGraph(len(g.V()) + len(h.V()))
    for g_edge in g.E():
        result.addedge(result.V()[g_edge.tail().getLabel()], result.V()[g_edge.head().getLabel()])
    offset = len(g.V())
    for h_edge in h.E():
        result.addedge(result.V()[h_edge.tail().getLabel() + offset], result.V()[h_edge.head().getLabel() + offset])
    return result


G = FastGraph(10)
G.addedge(G.V()[0], G.V()[1])
G.addedge(G.V()[1], G.V()[3])
G.addedge(G.V()[3], G.V()[6])
H = FastGraph(10)
H.addedge(H.V()[0], H.V()[9])
H.addedge(H.V()[2], H.V()[9])
H.addedge(H.V()[3], H.V()[9])
H.addedge(H.V()[4], H.V()[2])


# print(disjointunion(G, H))
print(disjoint_union(G, H))
