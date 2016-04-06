from final.fastgraphs import FastGraph


def disjoint_union(g, h):
    result = FastGraph(len(g.V()) + len(h.V()))
    for edge in g.E():
        result.addedge(result.V()[edge.tail().getLabel()], result.V()[edge.head().getLabel()])
    offset = len(g.V())
    for edge in h.E():
        result.addedge(result.V()[edge.tail().getLabel() + offset], result.V()[edge.head().getLabel() + offset])
    return result
