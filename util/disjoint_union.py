from graphImplementations.fastgraphs import *

#  Return a new graph that is the disjoint union of g and h
def disjointunion(g, h):
    result = g
    hcopy = h
    listofvertices = []
    length = len(g.V())
    for vertex in hcopy.V():
        vertex._label += length
        vertex.set_graph(result)
        node = result.addvertex(vertex.get_label())
        listofvertices.append(node)
    for edge in hcopy.E():
        for node in listofvertices:
            # print(type(node._label))
            if edge.tail().get_label() is node.get_label():
                edge.setTail(node)
            elif edge.head().get_label() is node.get_label():
                edge.setHead(node)
        result.addedge(edge.tail(), edge.head())
    # for node in result:
    #     print(type(node.getLabel()))
    return result




def disjoint_union(g, h):
    result = FastGraph(len(g.V()) + len(h.V()))
    for g_edge in g.E():
        result.addedge(result.V()[g_edge.tail().get_label()], result.V()[g_edge.head().get_label()])
    offset = len(g.V())
    for h_edge in h.E():
        result.addedge(result.V()[h_edge.tail().get_label() + offset], result.V()[h_edge.head().get_label() + offset])
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
